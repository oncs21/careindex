from fastapi import Request
from supabase import AsyncClient

def get_client(request: Request) -> AsyncClient:
    return request.app.state.client