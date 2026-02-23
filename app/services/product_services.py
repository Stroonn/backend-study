from app.models.product import Product
from app.utils.helpers import calculate_discount, is_positive, format_price

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
    
    def list_products(self):
        return self.repository.list_products()

    def delete_product(self, name):
        return self.repository.delete_product(name)

    def update_price(self, name, price):
        if price <= 0:
            raise ValueError("Preço inválido")
        return self.repository.update_product(name, price)
    
    def find_by_name(self, name):
        return self.repository.find_by_name(name)