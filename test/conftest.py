import sqlite3
import pytest
from fastapi.testclient import TestClient
from main_api import app, get_service
from app.repositories.product_sql_repository import ProductSQLiteRepository
from app.services.product_service import ProductService

@pytest.fixture
def client():

    connection = sqlite3.connect(":memory:", check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        desc TEXT,
        amount INTEGER,
        price REAL
    )
    """)
    connection.commit()

    repository = ProductSQLiteRepository(connection)
    service = ProductService(repository)

    def override_get_service():
        return service

    app.dependency_overrides[get_service] = override_get_service

    return TestClient(app)