from app.models.product import Product
from app.utils.helpers import calculate_discount, is_positive, format_price
from app.repositories.product_repository import ProductRepository
from app.repositories.mocky_repository import FakeRepository

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name, desc, amount, price):
        if not name.strip():
            raise ValueError("Nome obrigatório")

        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")

        if price <= 0:
            raise ValueError("Preço deve ser positivo")

        products = self.repository.load_products()
        new_product = Product(name, desc, amount, price)
        products.append(new_product)
        self.repository.save_products(products)
        return new_product