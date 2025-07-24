from langchain.schema import Document
from typing import List

# Utility to extract content from retriever results
def docs_to_str(docs: List[Document]) -> str:
    if isinstance(docs, list):
        # If docs are list of LangChain Document objects or dicts
        return "\n".join([d.page_content if hasattr(d, 'page_content') else str(d) for d in docs])
    return str(docs)