from fastapi import FastAPI
from app.routes import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")

@app.get("/")
async def root():
    return {"message": "FastAPI with MongoDB Authentication"}
