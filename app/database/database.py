import sqlite3

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        desc TEXT,
        amount INTEGER NOT NULL,
        price REAL NOT NULL
    )
    """)

    connection.commit()