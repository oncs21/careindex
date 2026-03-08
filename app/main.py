from fastapi import FastAPI
from app.api.router import router

from contextlib import asynccontextmanager
from app.api.dependencies.store import doc_store

from app.core.supabase_client import init_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client = await init_client()

    yield


app = FastAPI(
    title="CareIndex",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(router, prefix="/api/v1")


@app.get("/", tags=["Default"])
async def root():
    return {
        "API": "CareIndex API is now running!"
    }