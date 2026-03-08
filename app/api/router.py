from fastapi import APIRouter

from app.api.routes.documents.documents import router as documents_router
from app.api.routes.patients.patients import router as patients_router

router = APIRouter()

router.include_router(documents_router, prefix="")
router.include_router(patients_router, prefix="/p")