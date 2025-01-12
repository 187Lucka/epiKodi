from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/api/world")
async def hello_world():
    return {"hello": "world"}