from app.core.config import HF_TOKEN, REPO_ID
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

def createLLM(): 
    try:
        llm = HuggingFaceEndpoint(
            repo_id=REPO_ID,
            task="conversational",
            max_new_tokens=512,
            do_sample=False,
            repetition_penalty=1.03,
            huggingfacehub_api_token=HF_TOKEN
        )
        
        chat_llm = ChatHuggingFace(llm=llm, verbose=True)
        print("LLM Initialized")
        return chat_llm
    except Exception as e:
        print(f"LLM Initialization failed {str(e)}")
        return None

chat_llm = createLLM()

def build_context(docs):
    return ""

def generate_answer(query: str, chat_history: list):
    return ""

# texts = load_and_split_pdf("data")
# retriever = initialize_retriever(texts)

# print("LLM Chain Initialized")

# def build_context(docs):
#     return "\n".join([doc.page_content for doc in docs])[:1500]

# def generate_answer(query: str, chat_history: list):
#     try:
#         docs = retriever.invoke(query)
#         context = build_context(docs)
      
#         formatter = RunnableLambda(lambda d: prompt.format(**d))
#         chain = (
#             RunnableMap({
#                  "context": lambda x: x["context"],
#                  "chat_history": lambda x: x["chat_history"],
#                  "query": lambda x: x["query"]
#                          })
#             | formatter      # Convert dict to formatted string
#             | LLM            # HuggingFaceEndpoint expects a string prompt
#             | (lambda x: x.content if hasattr(x, "content") else x)
#                 )

#         inputs = {
#             "context": context,
#             "chat_history": chat_history,
#             "query": query
#         }

#         print("Calling LLM chain with inputs:", inputs)
#         result = chain.invoke(inputs)
#         print("LLM Response:", result)

#         return result 

#     except Exception as e:
#         import traceback
#         print("ERROR in generate_answer:", repr(e))
#         traceback.print_exc()
#         return "Sorry, something went wrong while generating the answer."
