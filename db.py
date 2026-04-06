import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  # change this
        database="ai_agent"
    )
    