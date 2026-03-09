from supabase import AsyncClient

class PatientRepository:
    def __init__(
        self, 
        db_client: AsyncClient
    ):
        self.db_client = db_client

    async def get_patient_by_id(
        self, 
        patient_id: int
    ):
        result = await self.db_client \
            .table("patients") \
            .select("*") \
            .eq("id", patient_id) \
            .execute()
        
        if not result.data:
            return None
        
        return result.data
    

    async def list_patients(
        self
    ):
        result = await self.db_client \
            .table("patients") \
            .select("*") \
            .execute()
        
        return result.data