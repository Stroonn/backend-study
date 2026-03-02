from datetime import date

from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_update_description():
    repo = FakeRepository()
    service = ProductService(repo)

    product = service.create_product(1, "Arroz", "Branco", 20, 10)
    updated_product = service.update_description(product.id, "Integral")

    assert updated_product is not None
    assert updated_product.name == "Arroz"
    assert updated_product.desc == "Integral"
    assert updated_product.amount == 20
    assert updated_product.price == 10
    assert updated_product.created_at == date.today()
    assert updated_product.updated_at is not None