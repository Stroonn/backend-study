from datetime import date

from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService


def test_update_price():
    repo = FakeRepository()
    service = ProductService(repo)

    # provide explicit id and a specific creation date
    product = service.create_product(1, "Arroz", "Branco", 20, 10)
    updated_product = service.update_price(product.id, 15)

    assert updated_product is not None
    assert updated_product.name == "Arroz"
    assert updated_product.desc == "Branco"
    assert updated_product.amount == 20
    assert updated_product.price == 15
    assert updated_product.created_at == date.today()
    assert updated_product.updated_at is not None