from fastapi import FastAPI


app = FastAPI(
    title="CareIndex",
    version="0.1.0",
)

@app.get("/", tags=["Default"])
async def root():
    return {
        "API": "CareIndex API is now running!"
    }