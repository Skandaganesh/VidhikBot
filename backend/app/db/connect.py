import psycopg2

def create_connection():
    try:
        # Replace these parameters with your database credentials
        connection = psycopg2.connect(
            database="vidhik_bot",
            user="shroudloaded",
            password="kadleesports",
            host="localhost",  # or your host IP
            port="5432"        # default PostgreSQL port
        )
        print("Connection to the database established successfully.")
        return connection
    except Exception as e:
        print(f"An error occurred: {e}")

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