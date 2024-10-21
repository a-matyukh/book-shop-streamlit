import sqlite3

def init():
    with sqlite3.connect("books.db") as connection:
        cursor = connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS BOOKS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book TEXT NOT NULL
        )
        """
        cursor.execute(query)

def get_all_books():
    with sqlite3.connect("books.db") as connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM BOOKS"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

def create_book(book_name):
    with sqlite3.connect("books.db") as connection:
        cursor = connection.cursor()
        query = f"INSERT INTO  BOOKS (book) VALUES ('{book_name}')"
        cursor.execute(query)
