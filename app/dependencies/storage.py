from fastapi import Depends
from supabase import AsyncClient

from app.services.storage_service import SupabaseStorageService
from app.dependencies.db import get_client


def get_storage_service(
    db_client: AsyncClient = Depends(get_client)
) -> SupabaseStorageService:
    return SupabaseStorageService(db_client)