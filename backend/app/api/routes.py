from fastapi import APIRouter,Request,HTTPException
from fastapi.responses import StreamingResponse
import uuid
from pydantic import BaseModel
from app.services.llm import generate_answer
from app.db.connect import create_connection
from app.services.summarizer import summarize_text
from elevenlabs import ElevenLabs
import os

class UserData(BaseModel):
    user_id: str

class UserResponse(BaseModel):
    user_id: str
    query: str

class textInput(BaseModel):
    text: str

connection = create_connection()

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=os.getenv('ELEVEN_API'))

router = APIRouter()

@router.post("/answer")
async def get_answer(userRes: UserResponse):
    """
    Endpoint to get answers for a query.

    Args:
        query (str): The user's query.

    Returns:
        dict: The response with the generated answer.
    """
    query = userRes.query
    user_id = userRes.user_id
    cursor = connection.cursor()
    cursor.execute(f"SELECT chat_history FROM user_chats WHERE user_id = '{user_id}'")
    chat_history = cursor.fetchone()[0]
    answer = generate_answer(query,chat_history)
    final_chat_history = summarize_text(str({"user_query": query,"chatbot_response": answer,"chat_history": chat_history}))
    cursor.execute(f"UPDATE user_chats SET chat_history = '{final_chat_history}' WHERE user_id = '{user_id}'")
    connection.commit()
    return {"query": query, "answer": answer}

@router.get("/start_session")
async def session_test():
    user_id = str(uuid.uuid4()) # Generate a unique user ID
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO user_chats (user_id) VALUES ('{user_id}')")
    connection.commit()
    return {"user_id": user_id}

@router.post("/end_session")
async def post_answer(user: UserData):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM user_chats WHERE user_id = '{user.user_id}'")
    connection.commit()
    return {"session ended": user.user_id, "status": "success"}  

@router.post("/speak")
async def generate_audio(input: textInput):
    try:
        audio = client.generate(
            text=input.text,
            voice="Alice",
            model="eleven_multilingual_v2"
        )

        # Ensure audio is in bytes (e.g., if it's a file-like object)
        if isinstance(audio, bytes):
            audio_data = audio
        else:
            # If audio is not in bytes, convert it appropriately
            audio_data = audio.read() if hasattr(audio, 'read') else None

        if audio_data is None:
            raise HTTPException(status_code=500, detail="Audio generation failed.")

        # Create a generator to stream audio data
        async def audio_stream():
            yield audio_data

        return StreamingResponse(audio_stream(), media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

































































































































































































