# app/main.py
from fastapi import FastAPI
from .diagrams import router as diagrams_router

app = FastAPI(title="Mermaid Diagram Generator")

app.include_router(diagrams_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Mermaid Diagram Generator API!"}

