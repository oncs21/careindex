from fastapi import FastAPI
from app.api.routes.documents.doucments import router as docs_router

from contextlib import asynccontextmanager
from app.api.dependencies.store import doc_store


@asynccontextmanager
async def lifespan(app: FastAPI):
    await doc_store.put(
        key="sample.txt",
        name="sample.txt",
        content_type="text/plain",
        data=b"Hello! This is a test doc."
    )

    await doc_store.put(
        key="sample2.txt",
        name="sample2.txt",
        content_type="text/plain",
        data=b"Hello! This is another test doc."
    )

    yield


app = FastAPI(
    title="CareIndex",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(docs_router, prefix="/api/v1")


@app.get("/", tags=["Default"])
async def root():
    return {
        "API": "CareIndex API is now running!"
    }