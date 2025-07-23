from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # Fix import here
from langchain_community.vectorstores import FAISS
import os

pdf1 = os.path.join("data", "law_1.pdf")
pdf2 = os.path.join("data", "law_2.pdf")

loader1 = PyPDFLoader(str(pdf1))
loader2 = PyPDFLoader(str(pdf2))

docs1 = loader1.load()
docs2 = loader2.load()

all_docs = docs1 + docs2

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = splitter.split_documents(all_docs)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")  # Use explicit model
db = FAISS.from_documents(texts, embeddings)

db.save_local("vector_store")
print("✅ Combined vector store saved in 'vector_store/'")
