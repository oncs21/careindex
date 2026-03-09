from fastapi import APIRouter, status, Depends, HTTPException, UploadFile, File
from fastapi.responses import Response

from app.repositories.documents.documents_repo import DocumentRepository
from app.services.storage_service import SupabaseStorageService
from app.dependencies.storage import get_storage_service
from app.dependencies.db import get_client
from app.dependencies.repositories import get_doc_repository

from supabase import AsyncClient

from starlette.responses import StreamingResponse
from starlette.background import BackgroundTask
from typing import List, Dict, Any

import httpx

router = APIRouter(tags=["Document"])

@router.get(
    "/doc/{doc_id}",
    status_code=status.HTTP_200_OK,
    name="get_original_document"
)
async def get_document(
    doc_id: int,
    db_client: AsyncClient = Depends(get_client),
    repository: DocumentRepository = Depends(get_doc_repository),
    storage_service: SupabaseStorageService = Depends(get_storage_service)
):
    data = await repository.get_document_by_id(doc_id)
    if not data:
        raise HTTPException(status_code=404, detail="Document does not exist")
    
    doc = data
    doc_url = await storage_service.get_document_url("patients", doc["storage_path"])

    if not doc_url or doc_url == "":
        raise HTTPException(status_code=404, detail="Document not found")

    async with httpx.AsyncClient() as client:
        request = client.build_request("GET", doc_url)
        response = await client.send(request, stream=True)

        return StreamingResponse(
            response.aiter_bytes(),
            media_type=response.headers.get("content-type", "application/octet-stream"),
            background=BackgroundTask(response.aclose)
        )
    

@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    name="upload_documents"
)
async def upload_documents(
    patient_id: int,
    payloads: List[Dict[str, Any]],
    files: List[UploadFile] = File(...),
    repository: DocumentRepository = Depends(get_doc_repository),
    storage_service: SupabaseStorageService = Depends(get_storage_service)
):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")
    
    if len(payloads) != len(files):
        raise HTTPException(status_code=400, detail="Number of payloads must match the number of files")
    
    results = []

    for idx, file in enumerate(files):
        try:
            content_type = file.content_type or "application/octet-stream"
            data = await file.read()

            if not data:
                results.append({
                    "filename": file.filename,
                    "status": "failed",
                    "error": "Empty file"
                })
                continue

            doc_type = payloads[idx]["doc_type"]

            ext_idx = file.filename.rfind('.')
            file_ext = ""
            if ext_idx != -1:
                file_ext = file.filename[ext_idx+1:]

            uploaded = await repository.upload_document(
                patient_id=patient_id,
                doc_title=file.filename,
                doc_type=doc_type,
                mime_type=file.content_type,
                file_ext=file_ext
            )

            if uploaded is None:
                results.append({
                    "filename": file.filename,
                    "status": "failed",
                    "error": "Could not create document record"
                })
                continue

            doc_id = uploaded["id"]

            storage_path = f"{patient_id}/documents/{uploaded['id']/{file.filename}}"

            await storage_service.upload_file(
                bucket_name="patients",
                file_bytes=data,
                content_type=file.content_type,
                storage_path=storage_path
            )

            updated_doc = await repository.update_document_storage(
                doc_id=doc_id,
                storage_path=storage_path,
                bucket_name="patients"
            )

            results.append({
                "document_id": doc_id,
                "filename": file.filename,
                "status": "uploaded",
                "document": updated_doc
            })
        
        except Exception as e:
            results.append({
                "filename": file.filename,
                "status": "failed",
                "error": str(e)
            })


    return {
        "patient_id": patient_id,
        "count": len(results),
        "results": results
    }
