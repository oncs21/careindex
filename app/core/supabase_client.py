from supabase import create_async_client, AsyncClient
from app.core.config import settings


client: AsyncClient | None = None


async def init_client(
    url: str = settings.client_url, 
    key: str = settings.client_key
):
    global client
    return await create_async_client(url, key)