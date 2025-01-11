import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain import PromptTemplate, LLMChain
import pprint

# Load variables from .env file
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
REPO_ID = os.getenv("REPO_ID")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

LLM = HuggingFaceEndpoint(repo_id=REPO_ID,max_length=250,temperature=0.7,token=HF_TOKEN)

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file.
loader = PyPDFLoader("./data/exampl.pdf")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)
print(len(texts))

# Using HuggingFaceEmbeddings for embeddings. You can choose other embeddings as well.
embeddings = HuggingFaceEmbeddings()
# Using FAISS as the vector database. You can choose other databases like FAISS.
db = FAISS.from_documents(texts, embeddings)

retriever = db.as_retriever(search_kwargs={"k": 3})  # Retrieve top 3 relevant documents

# Function to build the context from retrieved documents
def build_context(docs):
  context = ""
  for doc in docs:
    context += doc.page_content + "\n"  # Adjust as needed
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
    """
    Retrieves relevant documents based on the query, builds the context, 
    and uses the LLM chain to generate a response.

    Args:
        query (str): The user's query.

    Returns:
        str: The generated response from the LLM.
    """
    docs = retriever.get_relevant_documents(query)
    context = build_context(docs)
    result = llm_chain.invoke({"context": context, "query": query})
    return result["text"]  # Access the generated response

pprint.pprint(generate_answer("who all are eligible for the right to information act"))
