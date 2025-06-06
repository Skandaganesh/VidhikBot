from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.db.connect import create_connection

app = FastAPI(
    title="RAG Backend",
    description="A backend for Retrieval-Augmented Generation",
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

create_connection()
# Include API routes
app.include_router(router)