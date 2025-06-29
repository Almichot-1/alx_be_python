import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (update credentials if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''  # Add your MySQL password here if applicable
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create the database (should not fail if it already exists)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error connecting to the database: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
