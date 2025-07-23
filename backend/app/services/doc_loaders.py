from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

files = ["law_1"]

def create_documents() -> List[Document] | None:
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=250)
        documents: List[Document] = []
        for file in files:
            file_path = f"../../data/{file}.pdf"
            doc_loader = PyPDFLoader(file_path)
            docs = doc_loader.load_and_split(
                text_splitter=text_splitter
            )
            documents.extend(docs)
        n = len(documents)
        if n == 0:
            raise Exception("No documents were created")
        print(f"{n} Document chunks created")
    except Exception as e:
        print(f"an error occurred while creating documents: {e}")
        return None