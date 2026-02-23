
from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_create_product_success():
    repo = FakeRepository()
    service = ProductService(repo)

    product = service.create_product("Feijao", "Preto", 10, 5)

    assert len(repo.products) == 1
    print(repo.products)