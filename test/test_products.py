import pytest
from conftest import client

def test_list_products(client):

    response = client.get("/products")

    assert response.status_code == 200

def test_create_product(client):
    response = client.post(
        "/products",
        json={
            "name": "Feijao",
            "desc": "Preto",
            "amount": 10,
            "price": 5.5
        }
    )

    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Feijao"
    assert data["price"] == 5.5

def test_find_by_name(client, product):

    response = client.get(f"/products/{product['name']}")

    assert response.status_code == 200
    assert response.json()["name"] == "Feijao"

def test_update_name(client, product):

    response = client.put(
        f"/products/{product['id']}",
        params={"new_name": "Feijao do Sul"}
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Feijao do Sul"

def test_delete_product(client, product):

    response = client.delete(f"/products/{product['id']}")

    assert response.status_code == 200

