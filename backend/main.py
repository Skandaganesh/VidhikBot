# import os
# from dotenv import load_dotenv
# from langchain_huggingface import HuggingFaceEndpoint
# from PyPDF2 import PdfReader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.document_loaders import PyPDFLoader
# from langchain import PromptTemplate, LLMChain
# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn

# # Load variables from .env file
# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")
# REPO_ID = os.getenv("REPO_ID")

# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# LLM = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN)

#   path = Path(__file__).parent / "data" / "250883_english_01042024.pdf"
#   loader = PyPDFLoader(str(path))

# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# texts = text_splitter.split_documents(documents)
# print(len(texts))

# embeddings = HuggingFaceEmbeddings()
# db = FAISS.from_documents(texts, embeddings)

# retriever = db.as_retriever(search_kwargs={"k": 3})

# def build_context(docs):
#     context = ""
#     for doc in docs:
#         context += doc.page_content + "\n"
#     return context

# template = """
# You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
# Your goal is to provide helpful and informative responses to users' legal questions.

# Context: {context}

# Question: {query}

# Answer:
# """

# prompt = PromptTemplate(
#     input_variables=["context", "query"],
#     template=template,
# )

# llm_chain = LLMChain(prompt=prompt, llm=LLM)

# def generate_answer(query):
#     docs = retriever.get_relevant_documents(query)
#     context = build_context(docs)
#     result = llm_chain.invoke({"context": context, "query": query})
#     return result["text"]

# # FastAPI setup
# app = FastAPI()

# class Query(BaseModel):
#     question: str

# @app.get("/")
# def home():
#     return {"message": "VidhikBot is up and running"}

# @app.post("/ask")
# def ask(q: Query):
#     return {"answer": generate_answer(q.question)}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.document_loaders import PyPDFLoader
# from langchain import PromptTemplate, LLMChain
# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os
# import uvicorn

# load_dotenv()
# HF_TOKEN = os.getenv("HF_TOKEN")
# REPO_ID = os.getenv("REPO_ID")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# app = FastAPI()

# class Query(BaseModel):
#     question: str

# @app.get("/")
# def home():
#     return {"message": "VidhikBot is up and running"}

# @app.post("/ask")
# def ask(q: Query):
#     return {"answer": generate_answer(q.question)}

# # Globals
# retriever = None
# llm_chain = None

# def build_context(docs):
#     return "\n".join(doc.page_content for doc in docs)

# def generate_answer(query):
#     docs = retriever.get_relevant_documents(query)
#     context = build_context(docs)
#     result = llm_chain.invoke({"context": context, "query": query})
#     return result["text"]

# @app.on_event("startup")
# def load_model():
#     global retriever, llm_chain
#     path = Path(__file__).parent / "data" / "250883_english_01042024.pdf"
#     loader = PyPDFLoader(str(path))

#     documents = loader.load()
#     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
#     texts = text_splitter.split_documents(documents)
#     embeddings = HuggingFaceEmbeddings()
#     db = FAISS.from_documents(texts, embeddings)
#     retriever = db.as_retriever(search_kwargs={"k": 3})

#     template = """
#     You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
#     Your goal is to provide helpful and informative responses to users' legal questions.

#     Context: {context}

#     Question: {query}

#     Answer:
#     """
#     prompt = PromptTemplate(input_variables=["context", "query"], template=template)
#     llm_chain = LLMChain(prompt=prompt, llm=HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN))

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain import PromptTemplate, LLMChain
# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv
# import os
# import uvicorn
# from pathlib import Path

# from app.api.routes import router
# from fastapi.middleware.cors import CORSMiddleware
# from app.db.connect import create_connection

# app = FastAPI(
#     title="RAG Backend",
#     description="A backend for Retrieval-Augmented Generation",
#     version="1.0.0",
# )

# # Add CORS middleware to allow all origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allow all headers
# )

# create_connection()
# # Include API routes
# app.include_router(router)
# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")
# REPO_ID = os.getenv("REPO_ID")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# app = FastAPI()

# class Query(BaseModel):
#     question: str

# @app.get("/")
# def home():
#     return {"message": "VidhikBot is up and running"}

# @app.post("/ask")
# def ask(q: Query):
#     return {"answer": generate_answer(q.question)}

# # Globals
# retriever = None
# llm_chain = None

# def build_context(docs):
#     return "\n".join(doc.page_content for doc in docs)

# def generate_answer(query):
#     docs = retriever.get_relevant_documents(query)
#     context = build_context(docs)
#     result = llm_chain.invoke({"context": context, "query": query})
#     return result["text"]

# @app.on_event("startup")
# def load_resources():
#     global retriever, llm_chain

#     # Load vector store from disk (no PDF/embedding building)
#     embeddings = HuggingFaceEmbeddings()
#     vector_path = Path(__file__).parent / "vector_store"
#     db = FAISS.load_local(str(vector_path), embeddings)
#     retriever = db.as_retriever(search_kwargs={"k": 3})

#     # Define prompt
#     template = """
#     You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
#     Your goal is to provide helpful and informative responses to users' legal questions.

#     Context: {context}

#     Question: {query}

#     Answer:
#     """
#     prompt = PromptTemplate(input_variables=["context", "query"], template=template)
#     llm = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN)
#     llm_chain = LLMChain(prompt=prompt, llm=llm)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain.vectorstores import FAISS
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain import PromptTemplate, LLMChain
# from langchain_huggingface import HuggingFaceEndpoint
# from huggingface_hub import InferenceClient
# from dotenv import load_dotenv
# import os
# import uvicorn
# from pathlib import Path

# from app.api.routes import router
# from fastapi.middleware.cors import CORSMiddleware
# from app.db.connect import create_connection

# load_dotenv()
# HF_TOKEN = os.getenv("HF_TOKEN")
# REPO_ID = os.getenv("REPO_ID")
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

# app = FastAPI(
#     title="RAG Backend",
#     description="A backend for Retrieval-Augmented Generation",
#     version="1.0.0",
# )

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include API routes
# app.include_router(router)

# # DB connection
# create_connection()

# # Globals
# retriever = None
# llm_chain = None

# class Query(BaseModel):
#     question: str

# @app.get("/")
# def home():
#     return {"message": "VidhikBot is up and running"}

# @app.post("/ask")
# def ask(q: Query):
#     return {"answer": generate_answer(q.question)}

# def build_context(docs):
#     return "\n".join(doc.page_content for doc in docs)

# def generate_answer(query):
#     try:
#     docs = retriever.invoke(query)

#     context = build_context(docs)
#     result = llm_chain.invoke({"context": context, "query": query})
#     return result["text"]
#     except Exception as e:
#         print("Error during /answer:", str(e))
#         raise HTTPException(status_code=500, detail=str(e))

# @app.on_event("startup")
# def load_resources():
#     global retriever, llm_chain
#     vector_path = Path(__file__).parent / "vector_store"
#     embeddings = HuggingFaceEmbeddings()
#     db = FAISS.load_local(str(vector_path), embeddings, allow_dangerous_deserialization=True)
#     retriever = db.as_retriever(search_kwargs={"k": 3})

#     template = """
#     You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
#     Your goal is to provide helpful and informative responses to users' legal questions.

#     Context: {context}

#     Question: {query}

#     Answer:
#     """
#     prompt = PromptTemplate(input_variables=["context", "query"], template=template)
#     llm = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN)
#     llm_chain = LLMChain(prompt=prompt, llm=llm)

# if __name__ == "__main__":
#     uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from pathlib import Path
import os
import uvicorn

from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.db.connect import create_connection

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = os.getenv("REPO_ID")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

app = FastAPI(
    title="RAG Backend",
    description="A backend for Retrieval-Augmented Generation",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router)

# DB
create_connection()

# Globals
retriever = None
inference_client = None

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "VidhikBot is up and running"}

@app.post("/ask")
def ask(q: Query):
    try:
        return {"answer": generate_answer(q.question)}
    except Exception as e:
        print("Error during /ask:", str(e))
        raise HTTPException(status_code=500, detail=str(e))

def build_context(docs):
    return "\n".join(doc.page_content for doc in docs)

def generate_answer(query):
    docs = retriever.invoke(query)
    context = build_context(docs)

    prompt = f"""
You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
Your goal is to provide helpful and informative responses to users' legal questions.

Context: {context}

Question: {query}

Answer:
"""
    response = inference_client.conversational(
        inputs={"past_user_inputs": [], "generated_responses": [], "text": prompt}
    )
    return response.strip()

@app.on_event("startup")
def load_resources():
    global retriever, inference_client
    vector_path = Path(__file__).parent / "vector_store"
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.load_local(str(vector_path), embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 3})

    inference_client = InferenceClient(model=REPO_ID, token=HF_TOKEN)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
