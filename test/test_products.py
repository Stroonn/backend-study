from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_list_products():
    repo = FakeRepository()
    service = ProductService(repo)

    service.create_product(1,"Arroz", "Branco", 20, 10)
    service.create_product(2,"Feijao", "Preto", 10, 5)

    products = service.list_products()
    assert len(products) == 2
    assert products[0].name == "Arroz"
    assert products[1].name == "Feijao"
    