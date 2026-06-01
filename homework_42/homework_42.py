import pymysql
import os
from dotenv import load_dotenv
from pymysql.cursors import DictCursor

load_dotenv(".env")

db_name = "notes_app_121225ptm_Suligan"

config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'user'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
}

try:
    with pymysql.connect(**config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database {db_name} is created or already exists")

            cursor.execute(f"USE {db_name}")

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(250) NOT NULL,
            content TEXT NOT NULL)""")

            print("Table 'notes' created.")

            cursor.execute("""
            INSERT INTO notes (title, content)
            VALUES (%s, %s)""", (
                "Shopping list",
                "Milk, eggs, water"
            ))

            connection.commit()

            print("Note added: Shopping list")

        with connection.cursor(DictCursor) as cursor:
            cursor.execute("SELECT * FROM notes")

            notes = cursor.fetchall()

            for note in notes:
                print(f"Note added: {note['title']}")


except pymysql.MySQLError as e:
    print(f"Error occured with Database: {e}")
