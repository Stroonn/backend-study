from app.models.product import Product
from app.utils.helpers import calculate_discount, is_positive, format_price

class ProductService:
    def create_product(self, name:str, desc:str, amount:int, price:float) -> Product:
        if not is_positive(price):
                raise ValueError("Price must be positive!")
        if not is_positive(amount):
                raise ValueError("Amount must be positive!")
        if not name:
            raise ValueError("Name cannot be empty")
        price = calculate_discount(price, 10)
        return Product(name, desc, amount, price)