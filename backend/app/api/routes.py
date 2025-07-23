from fastapi import APIRouter
from app.api.controllers import start_session, end_session, get_answer
from app.api.models import UserData, UserResponse

chatbot_router = APIRouter()

@chatbot_router.get("/start_session")
async def handle_request():
    return await start_session()

@chatbot_router.post("/end_session")
async def handle_request(body: UserData):
    return await end_session(body)

@chatbot_router.post("/answer")
async def handle_request(body: UserResponse):
    return await get_answer(body)
