import pytest
from conftest import client

def test_list_products_pagination(client):

    for i in range(5):
        client.post(
            "/products",
            json={
                "name": f"Produto{i}",
                "desc": "Teste",
                "amount": 10,
                "price": 5.0
            }
        )

    response = client.get("/products?skip=0&limit=2")

    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert len(data["data"]) == 2