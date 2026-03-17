import pytest
from conftest import client

def test_find_product_not_found(client):

    response = client.get("/products/ProdutoInexistente")

    assert response.status_code == 404

def test_update_product_not_found(client):

    response = client.put(
        "/products/999",
        params={"new_name": "NovoNome"}
    )

    assert response.status_code == 404

def test_delete_product_not_found(client):

    response = client.delete("/products/999")

    assert response.status_code == 404

def test_create_product_invalid_price(client):

    response = client.post(
        "/products",
        json={
            "name": "Feijao",
            "desc": "Preto",
            "amount": 10,
            "price": -5
        }
    )

    assert response.status_code == 422

def test_create_product_invalid_amount(client):

    response = client.post(
        "/products",
        json={
            "name": "Feijao",
            "desc": "Preto",
            "amount": -10,
            "price": 5.5
        }
    )

    assert response.status_code == 422

def test_create_product_invalid_name(client):

    response = client.post(
        "/products",
        json={
            "name": "",
            "desc": "Preto",
            "amount": 10,
            "price": 5.5
        }
    )

    assert response.status_code == 422