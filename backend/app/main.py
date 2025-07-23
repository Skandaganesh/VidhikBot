from fastapi import FastAPI
from app.api.routes import chatbot_router
from fastapi.middleware.cors import CORSMiddleware
# from app.db.connect import connectDB

app = FastAPI(
    title="Vidhik: Indian Law Chatbot Backend",
    description="RAG-based Indian law chatbot backend",
    version="1.0.0",
)

# Add CORS middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(chatbot_router, prefix="/chat", tags=["Chatbot"])