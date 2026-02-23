from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService


def test_delete_product():
    repo = FakeRepository()
    service = ProductService(repo)

    service.create_product("Feijao", "Preto", 10, 5)
    service.list_products()
    service.delete_product("Feijao")

    assert len(repo.products) == 0