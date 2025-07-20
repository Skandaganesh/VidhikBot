import psycopg2
import os

def create_connection():
    try:
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError("DATABASE_URL environment variable not set")

        connection = psycopg2.connect(db_url)
        print("Connection to the database established successfully.")
        return connection
    except Exception as e:
        print(f"An error occurred: {e} ")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Database connection closed.")

# create_connection()
# Main execution flow
# if __name__ == "__main__":
#     conn = create_connection()
#     if conn:
#         close_connection(conn)