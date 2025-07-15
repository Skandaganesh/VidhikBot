from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from pathlib import Path

# Step 1: Load both PDFs
pdf1 = Path("data") / "250883_english_01042024.pdf"
pdf2 = Path("data") / "250884_2_english_01042024.pdf"

loader1 = PyPDFLoader(str(pdf1))
loader2 = PyPDFLoader(str(pdf2))

docs1 = loader1.load()
docs2 = loader2.load()

# Step 2: Combine documents
all_docs = docs1 + docs2

# Step 3: Split into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = splitter.split_documents(all_docs)

# Step 4: Create vector store
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(texts, embeddings)

# Step 5: Save to disk
db.save_local("vector_store")
print("✅ Combined vector store saved in 'vector_store/'")
