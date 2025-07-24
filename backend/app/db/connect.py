from pymongo import MongoClient
from app.core.config import DATABASE_URL

def connectDB():
    try:
        if not DATABASE_URL:
            raise ValueError("DATABASE_URL environment variable not set")

        client = MongoClient(DATABASE_URL)
        print("Connection to the database established successfully.")
        return client["vidhik_bot"]
    except Exception as e:
        print(f"An error occurred: {e} ")
        return None

db = connectDB()