from app.database.connection import get_connection
from app.database.database import create_tables

def init_db():
    conn = get_connection()
    create_tables(conn)
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized.")