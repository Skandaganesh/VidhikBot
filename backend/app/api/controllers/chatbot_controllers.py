from fastapi.responses import JSONResponse
from app.services.llm import generate_answer
from app.db.connect import connectDB
from app.services.summarizer import summarize_text
from app.api.models import UserData, UserResponse
import uuid

connection = connectDB()

async def start_session() -> JSONResponse:
    try:
        user_id = str(uuid.uuid4())
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user_chats (user_id) VALUES (%s)", (user_id,))
        connection.commit()
        return {"user_id": user_id}
    except Exception as e:
        raise JSONResponse(status_code=500, detail=str(e))

async def end_session(user: UserData) -> JSONResponse:
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM user_chats WHERE user_id = %s", (user.user_id,))
        connection.commit()
        return {"session_ended": user.user_id, "status": "success"}
    except Exception as e:
        raise JSONResponse(status_code=500, detail=str(e))
    
async def get_answer(userRes: UserResponse) -> JSONResponse:
    user_id = userRes.user_id
    query = userRes.query

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT chat_history FROM user_chats WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        chat_history = result[0] if result else ""

        answer = generate_answer(query, chat_history)
        final_chat_history = summarize_text(str({
            "user_query": query,
            "chatbot_response": answer,
            "chat_history": chat_history
        }))

        if result:
            cursor.execute("UPDATE user_chats SET chat_history = %s WHERE user_id = %s", (final_chat_history, user_id))
        else:
            cursor.execute("INSERT INTO user_chats (user_id, chat_history) VALUES (%s, %s)", (user_id, final_chat_history))

        connection.commit()
        return {"query": query, "answer": answer}

    except Exception as e:
        print("Error during /answer:", str(e))
        raise JSONResponse(status_code=500, detail=str(e))