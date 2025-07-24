from fastapi import FastAPI
from app.api.routers.chatbot_router import chatbot_router
from app.api.routers.knowledge_base_router import knowledge_base_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import CLIENT_URL, DEV_CLIENT_URL

app = FastAPI(
    title="Vidhik: Indian Law Chatbot Backend",
    description="RAG-based Indian law chatbot backend",
    version="1.0.0",
)

# production
origins = [CLIENT_URL]
# development
# origins = [DEV_CLIENT_URL]

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get('/')
async def check_health():
    print("Hello, I am up and running")
    return "Hello Client, I am up and running"

# Include API routes
app.include_router(knowledge_base_router, prefix="/knowledge", tags=["Knowledge Base"])
app.include_router(chatbot_router, prefix="/chat", tags=["Chatbot"])