from app.repositories.mocky_repository import FakeRepository
from app.services.product_services import ProductService

def test_order_by_price():
    repo = FakeRepository()
    service = ProductService(repo)

    service.create_product(1,"Arroz", "Branco", 20, 10)
    service.create_product(2,"Feijao", "Preto", 10, 5)  
    products = service.order_by_price(ascending=True)
    assert len(products) == 2
    assert products[0].name == "Feijao"
    assert products[1].name == "Arroz"
    products = service.order_by_price(ascending=False)
    assert len(products) == 2
    assert products[0].name == "Arroz"
    assert products[1].name == "Feijao"