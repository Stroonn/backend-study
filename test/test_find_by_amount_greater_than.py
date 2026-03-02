from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_find_by_amount_greater_than():
    repo = FakeRepository()
    service = ProductService(repo)

    service.create_product(1,"Arroz", "Branco", 20, 10)
    service.create_product(2,"Feijao", "Preto", 10, 5) 
    products = service.find_by_amount_greater_than(10)

    assert len(products) == 1
    assert products[0].name == "Arroz"