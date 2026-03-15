from fastapi import APIRouter, status, Depends, HTTPException

from app.dependencies.db import get_client
from app.dependencies.repositories import get_patient_repository, get_doc_repository

from app.repositories.patients.patients_repo import PatientRepository
from app.repositories.documents.documents_repo import DocumentRepository

from supabase import AsyncClient

router = APIRouter(tags=["Patient"])

@router.get(
    "/patients",
    status_code=status.HTTP_200_OK,
    name="get_patients"
)
async def get_patients(
    db_client: AsyncClient = Depends(get_client)
):
    result = await db_client.table("patients").select("*").execute()
    return result.data


@router.get(
    "/patient/{patient_id}",
    status_code=status.HTTP_200_OK,
    name="get_patient"
)
async def get_patient(
    patient_id: int,
    db_client: AsyncClient = Depends(get_client)
):
    result = await db_client.table("patients") \
    .select("*") \
    .eq("id", patient_id) \
    .execute()

    return result.data


@router.get(
    "/patient/{patient_id}/docs",
    status_code=status.HTTP_200_OK,
    name="get_patient_docs"
)
async def get_patient_docs(
    patient_id: int,
    db_client: AsyncClient = Depends(get_client),
    repository: DocumentRepository = Depends(get_doc_repository)
):
    docs = await repository.get_documents_by_patient(patient_id)
    return docs

    