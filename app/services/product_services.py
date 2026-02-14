from app.models.product import Product

class ProductService:
    def create_product(self, name:str, desc:str, amount:int, price:float) -> Product:
        return Product(name, desc, amount, price)