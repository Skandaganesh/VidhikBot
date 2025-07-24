from fastapi.responses import JSONResponse
from app.services.tasks import generate_answer
from app.db.connect import db
from app.api.models import UserData, UserResponse
import uuid

user_chats = db["user_chats"]

async def start_session() -> JSONResponse:
    try:
        print("starting new session...")
        user_id = str(uuid.uuid4())
        user_chats.insert_one({"user_id": user_id, "chat_history": []})
        print("started new session.")
        return JSONResponse(
            status_code=201,
            content={"data": {"user_id": user_id}, "message": "session started", "error": None}
        )
    except Exception:
        print("error in starting new session.")
        return JSONResponse(
            status_code=500,
            content={"data": None, "message": "session was not initiated", "error": "an error in starting session"}
        )

async def end_session(user: UserData) -> JSONResponse:
    try:
        print("ending existing session...")
        result = user_chats.delete_one({"user_id": user.user_id})
        if result.deleted_count:
            print("ended session.")
            return JSONResponse(
                status_code=200,
                content={"data": {"user_id": user.user_id}, "message": "session ended", "error": None}
            )
        else:
            print("session not found and ended.")
            return JSONResponse(
                status_code=404,
                content={"data": None, "message": "session not found", "error": "no session exists"}
            )
    except Exception:
        print("error in ending session.")
        return JSONResponse(
            status_code=500,
            content={"data": None, "message": "failed to end session", "error": "an error occurred during session termination"}
        )

async def get_answer(userRes: UserResponse) -> JSONResponse:
    user_id = userRes.user_id
    query = userRes.query

    try:
        print("generating answer...")
        record = user_chats.find_one({"user_id": user_id})
        if record is None:
            raise Exception("User not found")
        chat_history = record.get("chat_history", []) if record else []

        # retrieve only the textual history for the LLM
        history_text = "\n".join(
            [f"User: {h['user_query']}\nChatbot: {h['chatbot_response']}" for h in chat_history]
        )
        print("retreived chat history.")

        answer = await generate_answer(query, history_text)

        # append new Q&A to history array
        user_chats.update_one(
            {"user_id": user_id},
            {"$push": {"chat_history": {"user_query": query, "chatbot_response": answer}}},
            upsert=True
        )

        return JSONResponse(
            status_code=200,
            content={"data": { "answer": answer}, "message": "answer generated", "error": None}
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"data": None, "message": "error during answer generation", "error": "an error occurred while processing request"}
        )
