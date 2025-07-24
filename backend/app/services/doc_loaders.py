from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Optional
from langchain.schema import Document
import os

files = ["law_1"]

async def create_documents() -> Optional[List[Document]]:
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
        documents: List[Document] = []
        for file in files:
            file_path = os.path.join("data", f"{file}.pdf")
            print(f"File Path: {file_path}")
            doc_loader = PyPDFLoader(file_path)
            docs = doc_loader.load_and_split(
                text_splitter=text_splitter
            )
            documents.extend(docs)
            print(f"Chunk created for file: {file}")
        n = len(documents)
        if n == 0:
            raise Exception("No documents were created")
        print(f"{n} Document chunks created")
        return documents
    except Exception as e:
        print(f"an error occurred while creating documents: {e}")
        return None