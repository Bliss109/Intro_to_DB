import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (update with your MySQL user & password)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: Could not connect to MySQL server or create database.\nDetails: {e}")

    finally:
        # Close connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
