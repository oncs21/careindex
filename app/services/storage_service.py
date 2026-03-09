from supabase import AsyncClient

class SupabaseStorageService:
    def __init__(
        self, 
        db_client: AsyncClient
    ):
        self.db_client = db_client

    
    async def get_document_url(
        self,
        bucket_name: str,
        storage_path: str
    ):
        return await self.db_client.storage.from_(bucket_name).get_public_url(storage_path)
    

    async def upload_file(
        self,
        bucket_name: str,
        file_bytes: bytes,
        content_type: str,
        storage_path: str
    ):
        
        result = await self.db_client.storage.from_(bucket_name).upload(
            path=storage_path,
            file=file_bytes,
            file_options={
                "content-type": content_type
            }
        )

        return result
    

    async def delete_file(
        self,
        bucket_name: str,
        storage_path: str
    ):
        return await self.db_client.storage.from_(bucket_name).remove([storage_path])