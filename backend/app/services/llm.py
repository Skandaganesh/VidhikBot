from app.core.config import HF_TOKEN, REPO_ID
from langchain_huggingface import HuggingFaceEndpoint
from app.core.templates import prompt
from langchain import LLMChain
import os

from app.services.retriever import initialize_retriever

# Initialize HuggingFace Endpoint
LLM = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN)

llm_chain = LLMChain(prompt=prompt, llm=LLM)

# Load documents and retriever
from app.utils.pdf_loader import load_and_split_pdf

texts = load_and_split_pdf("/workspaces/VidhikBot/backend/data")
retriever = initialize_retriever(texts)

print("LLM Chain Initialized")

def build_context(docs):
    """
    Builds context from retrieved documents.
    """
    return "\n".join([doc.page_content for doc in docs])

def generate_answer(query,chat_history):
    """
    Generates an answer based on the user's query.
    """
    docs = retriever.get_relevant_documents(query)
    context = build_context(docs)
    result = llm_chain.invoke({"context": context, "chat_history": chat_history,"query": query})
    return result["text"]
