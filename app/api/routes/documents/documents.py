from fastapi import APIRouter, status, Depends, HTTPException, UploadFile, File
from fastapi.responses import Response
from app.storage.temp.inmemory import InMemoryDocumentStore
from app.api.dependencies.store import get_doc_store
from starlette.responses import FileResponse
from typing import List, Dict

router = APIRouter(tags=["Document"])

@router.get(
    "/doc/{doc_name}",
    status_code=status.HTTP_200_OK,
    name="get_document"
)
async def get_document(
    doc_name: str,
    repository: InMemoryDocumentStore = Depends(get_doc_store)
):
    if not doc_name:
        raise HTTPException(status_code=400, detail="Invalid document name")
    
    try:
        return await repository.preview_response(doc_name)
    except KeyError:
        raise HTTPException(status_code=404, detail="Document not found")  
    

@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    name="upload_documents"
)
async def upload_documents(
    files: List[UploadFile] = File(...),
    repository: InMemoryDocumentStore = Depends(get_doc_store)
):
    if not len(files):
        raise HTTPException(status_code=400, detail="No files uploaded")
    
    res: Dict[str, any] = {}

    for file in files:
        content_type = file.content_type or "application/octet-stream"
        data = await file.read()

        try:
            stored = await repository.put(
                key=file.filename,
                name=file.filename,
                content_type=content_type,
                data=data
            )
    
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to store {file.filename}") from e

        res[file.filename] = {
            **stored,
            "content_type": content_type,
            "original_name": file.filename
        }

    return res


@router.delete(
    "/{doc_name}"
)
async def delete_document(
    doc_name: str,
    repository: InMemoryDocumentStore = Depends(get_doc_store)
):
    if not doc_name:
        raise HTTPException(status_code=400, detail="Invalid document name")
    
    return await repository.delete(doc_name)


@router.get(
    "/doc/{doc_name}/download",
    status_code=status.HTTP_200_OK,
    name="download_document"
)
async def download_document(
    doc_name: str,
    repository: InMemoryDocumentStore = Depends(get_doc_store)
):
    if not doc_name:
        raise HTTPException(status_code=400, detail="Invalid document name")
    
    doc_details = {}
    
    try:
        doc_details = await repository.get(doc_name)
    except KeyError:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return Response(
        content=doc_details["bytes"],
        media_type=doc_details["content_type"],
        headers={
            "Content-Disposition": f'attachment; filename="{doc_details["name"]}"'
        }
    )