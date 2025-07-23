from fastapi import APIRouter
from app.api.controllers.knowledge_base_controllers import create_knowledge_base, check_knowledge_base
from app.api.models import KnowlegdeQuery

knowledge_base_router = APIRouter()

@knowledge_base_router.get("/create")
async def handle_request():
    return await create_knowledge_base()

@knowledge_base_router.post("/check")
async def handle_request(body: KnowlegdeQuery):
    return await check_knowledge_base(body)