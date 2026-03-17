import sqlite3

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        desc TEXT,
        amount INTEGER,
        price REAL
    )
    """)

    connection.commit()