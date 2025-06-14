import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate, LLMChain
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Load variables from .env file
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = os.getenv("REPO_ID")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

LLM = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=250, temperature=0.7, token=HF_TOKEN)

loader = PyPDFLoader("/workspaces/VidhikBot/backend/data/250883_english_01042024.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)
print(len(texts))

embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(texts, embeddings)

retriever = db.as_retriever(search_kwargs={"k": 3})

def build_context(docs):
    context = ""
    for doc in docs:
        context += doc.page_content + "\n"
    return context

template = """
You are an Indian Law Assistance Chatbot. You have access to a vast knowledge base of Indian laws, acts, and sections. 
Your goal is to provide helpful and informative responses to users' legal questions.

Context: {context}

Question: {query}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["context", "query"],
    template=template,
)

llm_chain = LLMChain(prompt=prompt, llm=LLM)

def generate_answer(query):
    docs = retriever.get_relevant_documents(query)
    context = build_context(docs)
    result = llm_chain.invoke({"context": context, "query": query})
    return result["text"]

# FastAPI setup
app = FastAPI()

class Query(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "VidhikBot is up and running"}

@app.post("/ask")
def ask(q: Query):
    return {"answer": generate_answer(q.question)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
