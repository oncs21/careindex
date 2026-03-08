from fastapi import APIRouter, status, Depends, HTTPException
from app.api.dependencies.db import get_client
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