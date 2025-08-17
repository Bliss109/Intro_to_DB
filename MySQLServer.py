import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (update user & password as per your setup)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server or create database.\nDetails: {e}")

    finally:
        # Close connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")   # optional debug message

if __name__ == "__main__":
    create_database()
