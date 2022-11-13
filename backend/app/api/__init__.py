from fastapi import APIRouter
from .endpoints import router as v1

root = APIRouter()

@root.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to mapmymap."}

root.include_router(router=v1)
