from supabase import AsyncClient

class DocumentRepository:
    def __init__(
        self, 
        db_client: AsyncClient
    ):
        self.db_client = db_client

    async def get_document_by_id(
        self, 
        doc_id: int,
    ):
        result = await self.db_client \
        .table("documents") \
        .select("*") \
        .eq("id", doc_id) \
        .execute()

        print(result.data)

        if not result.data:
            return None
        
        return result.data[0]
    

    async def get_documents_by_patient(
        self,
        patient_id: int
    ):
        result = await self.db_client \
        .table("documents") \
        .select("*") \
        .eq("patient_id", patient_id) \
        .execute()

        if not result.data:
            return None
        
        return result.data
    

    async def upload_document(
        self,
        patient_id: int,
        doc_title: str,
        doc_type: str,
        mime_type: str,
        file_ext: str,
    ):
        payload = {
            "patient_id": patient_id,
            "title": doc_title,
            "doc_type": doc_type,
            "mime_type": mime_type,
            "file_ext": file_ext
        }

        result = await self.db_client \
        .table("documents") \
        .insert(payload) \
        .execute()

        if not result.data:
            return None
        
        return result.data[0]
    

    async def update_document_storage(
        self,
        doc_id: int,
        storage_path: str,
        bucket_name: str
    ):
        payload = {
            "storage_path": storage_path
        }

        result = await self.db_client \
        .table("documents") \
        .update(payload) \
        .eq("id", doc_id) \
        .execute()

        if not result.data:
            return None
        
        return result.data[0]