from fastapi import Depends
from supabase import AsyncClient

from app.dependencies.db import get_client
from app.repositories.documents.documents_repo import DocumentRepository
from app.repositories.patients.patients_repo import PatientRepository


def get_doc_repository(
    db_client: AsyncClient = Depends(get_client)
) -> DocumentRepository:
    return DocumentRepository(db_client)


def get_patient_repository(
    db_client: AsyncClient = Depends(get_client)
) -> PatientRepository:
    return PatientRepository(db_client)