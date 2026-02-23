from app.repositories.product_repository import ProductRepository
from app.models.product import Product
from pathlib import Path

def test_save_and_load_products(tmp_path):
    # cria caminho temporário
    file_path = tmp_path / "products.json"

    repo = ProductRepository(file_path)

    products = [
        Product("Feijao", "Preto", 10, 5.0),
        Product("Arroz", "Branco", 20, 7.5),
    ]

    repo.save_products(products)

    loaded = repo.load_products()

    assert len(loaded) == 2
    assert loaded[0].name == "Feijao"
    assert loaded[1].price == 7.5