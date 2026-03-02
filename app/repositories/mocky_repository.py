from app.models.product import Product
from datetime import date


class FakeRepository:
    def __init__(self):
        self.products = []

    def load_products(self):
        return self.products

    def save_products(self, products):
        self.products = products

    def list_products(self):
        return self.load_products()

    def find_by_name(self, name: str) -> Product | None:
        products = self.load_products()
        for p in products:
            if p.name == name:
                return p
        return None
    
    def find_by_price_less_than(self, price: float) -> list[Product]:
        products = self.load_products()
        return [p for p in products if p.price < price]
    
    def find_by_amount_greater_than(self, amount: int) -> list[Product]:
        products = self.load_products()
        return [p for p in products if p.amount > amount]
    
    def order_by_price(self, ascending=True) -> list[Product]:
        products = self.load_products()
        return sorted(products, key=lambda p:p.price, reverse=not ascending)
    
    def update_name(self, id: int, new_name: str) -> Product | None:
        products = self.load_products()
        updated_product = None

        for p in products:
            if p.id == id:
                p.name = new_name
                p.updated_at = date.today()
                updated_product = p

        if updated_product:
            self.save_products(products)

        return updated_product
    
    def update_desc(self, id: int, new_desc: str) -> Product | None:
        products = self.load_products()
        updated_product = None

        for p in products:
            if p.id == id:
                p.desc = new_desc
                p.updated_at = date.today()
                updated_product = p

        if updated_product:
            self.save_products(products)

        return updated_product
    
    def update_amount(self, id: int, new_amount: int) -> Product | None:
        products = self.load_products()
        updated_product = None

        for p in products:
            if p.id == id:
                p.amount = new_amount
                p.updated_at = date.today()
                updated_product = p

        if updated_product:
            self.save_products(products)

        return updated_product
    
    def update_price(self, id: int, new_price: float) -> Product | None:
        products = self.load_products()
        updated_product = None

        for p in products:
            if p.id == id:
                p.price = new_price
                p.updated_at = date.today()
                updated_product = p

        if updated_product:
            self.save_products(products)

        return updated_product
    
    def delete_product(self, id: int) -> bool:
        products = self.load_products()
        new_products = [p for p in products if p.id != id]

        if len(new_products) == len(products):
            return False

        self.save_products(new_products)
        return True