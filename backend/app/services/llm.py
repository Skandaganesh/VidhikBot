# from app.core.config import HF_TOKEN, REPO_ID
# from langchain_huggingface import HuggingFaceEndpoint
# from app.core.templates import prompt
# from langchain import LLMChain

# from app.services.retriever import initialize_retriever
# from app.utils.pdf_loader import load_and_split_pdf

# # Validate Hugging Face Token
# if not HF_TOKEN:
#     raise ValueError("HF_TOKEN is not set. Check your environment variables.")

# # Initialize HuggingFace Endpoint
# LLM = HuggingFaceEndpoint(
#     repo_id=REPO_ID,
#     max_length=250,
#     temperature=0.7,
#     token=HF_TOKEN
# )

# # Create LLM Chain with the prompt
# llm_chain = LLMChain(prompt=prompt, llm=LLM)

# # Load and split PDFs
# texts = load_and_split_pdf("data")
# retriever = initialize_retriever(texts)

# print("LLM Chain Initialized")

# def build_context(docs):
#     return "\n".join([doc.page_content for doc in docs])

# def generate_answer(query, chat_history):
#     try:
#         print("Generating answer...")
#         print("Query:", query)

#         docs = retriever.invoke(query)

#         if not docs:
#             print("No documents found.")
#             return "I couldn't find anything relevant in the documents."

#         context = build_context(docs)
#         print("Context built. Length:", len(context))

#         inputs = {
#             "context": context,
#             "chat_history": chat_history,
#             "query": query
#         }

#         print("Calling LLMChain with inputs:", inputs)

#         result = llm_chain.invoke(inputs)

#         print("LLM Response:", result)

#         if isinstance(result, dict) and "text" in result:
#             return result["text"]
#         elif isinstance(result, str):
#             return result
#         else:
#             print("Unexpected result type:", type(result))
#             return "Sorry, I received an unexpected response format from the model."

#     except Exception as e:
#         print("ERROR in generate_answer:", repr(e))
#         return "Sorry, something went wrong while generating the answer."
from app.core.config import HF_TOKEN, REPO_ID
from langchain_huggingface import HuggingFaceEndpoint
from app.core.templates import prompt  # PromptTemplate
from app.services.retriever import initialize_retriever
from app.utils.pdf_loader import load_and_split_pdf
from langchain_core.runnables import RunnableMap, RunnableLambda

if not HF_TOKEN:
    raise ValueError("HF_TOKEN is not set. Check your environment variables.")

LLM = HuggingFaceEndpoint(
    repo_id=REPO_ID,
    max_new_tokens=512,
    temperature=0.7,
    huggingfacehub_api_token=HF_TOKEN  # ✅ Safer alternative
)


texts = load_and_split_pdf("data")
retriever = initialize_retriever(texts)

print("LLM Chain Initialized")

def build_context(docs):
    return "\n".join([doc.page_content for doc in docs])[:1500]

def generate_answer(query: str, chat_history: list):
    try:
        docs = retriever.invoke(query)
        context = build_context(docs)
      
        formatter = RunnableLambda(lambda d: prompt.format(**d))
        chain = (
            RunnableMap({
                 "context": lambda x: x["context"],
                 "chat_history": lambda x: x["chat_history"],
                 "query": lambda x: x["query"]
                         })
            | formatter      # Convert dict to formatted string
            | LLM            # HuggingFaceEndpoint expects a string prompt
            | (lambda x: x.content if hasattr(x, "content") else x)
                )

        inputs = {
            "context": context,
            "chat_history": chat_history,
            "query": query
        }

        print("Calling LLM chain with inputs:", inputs)
        result = chain.invoke(inputs)
        print("LLM Response:", result)

        return result 

    except Exception as e:
        import traceback
        print("ERROR in generate_answer:", repr(e))
        traceback.print_exc()
        return "Sorry, something went wrong while generating the answer."
