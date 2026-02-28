from fastapi import APIRouter, status, Depends, HTTPException
from app.storage.temp.inmemory import InMemoryDocumentStore
from app.api.dependencies.store import get_doc_store
from starlette.responses import FileResponse

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