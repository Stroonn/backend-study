
import pytest
from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_create_product_amount_error():
    repo = FakeRepository()
    service = ProductService(repo)

    with pytest.raises(ValueError):
        service.create_product("Feijao", "Preto", -10, 5)