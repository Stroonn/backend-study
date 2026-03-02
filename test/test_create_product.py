from datetime import date

from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_create_product():
    repo = FakeRepository()
    service = ProductService(repo)

    product = service.create_product(1, "Arroz", "Branco", 20, 10)

    assert product.id == 1
    assert product.name == "Arroz"
    assert product.desc == "Branco"
    assert product.amount == 20
    assert product.price == 10
    assert product.created_at == date.today()
    assert product.updated_at == None