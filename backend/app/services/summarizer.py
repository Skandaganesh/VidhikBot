# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text, max_length=1000, min_length=15):
#     """
#     Summarizes the given text using the facebook/bart-large-cnn model.

#     Parameters:
#     - text (str): The text to be summarized.
#     - max_length (int): The maximum length of the summary.
#     - min_length (int): The minimum length of the summary.

#     Returns:
#     - str: The summarized text.
#     """
#     # Initialize the summarization pipeline
    
#     # Generate the summary
#     summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
#     return summary[0]['summary_text']

# # Example usage
# # text = '''The Clockmaker's Secret
# #  In the heart of the quiet town of Elmsworth, where cobblestone streets wound like veins through clusters of red-brick buildings, there stood a peculiar shop on the corner of Wren Street. Above its arched wooden door, a sign swayed gently in the breeze: "The Clockmaker’s Haven."
# #  Old Mr. Thaddeus Grey, the owner, was a reclusive man with a penchant for precision. His hands, worn yet steady, crafted timepieces so intricate that even the most skilled artisans in neighboring cities spoke of his work in hushed reverence. But what the townsfolk didn’t know—what no one knew—was that every clock he made carried a fragment of something far more extraordinary.
# #  One winter evening, as the first snow blanketed Elmsworth, a young woman named Lila stumbled into the shop. Her auburn hair was flecked with frost, and her cheeks were flushed from the cold. She carried a broken pocket watch, its silver casing tarnished but glinting faintly under the shop’s flickering lantern.'''

# # summary_result = summarize_text(text)
# # print(summary_result)
import requests
import os

HF_TOKEN = os.getenv("HF_TOKEN")  # Set this in your .env
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def summarize_text(text, max_length=1000, min_length=15):
    payload = {
        "inputs": text,
        "parameters": {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": False
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()[0]["summary_text"]
