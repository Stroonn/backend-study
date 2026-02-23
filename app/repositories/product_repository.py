import json
from pathlib import Path
from app.models.product import Product

#DATA_PATH = Path("data/products.json")

class ProductRepository:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_products(self) -> list[Product]:
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r") as file:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            data = json.load(file)

        return [Product(**item) for item in data]

    def save_products(self, products: list[Product]) -> None:
        data = [product.__dict__ for product in products]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def list_products(self) -> list[Product]:
        return self.load_products()

    def find_by_name(self, name: str) -> Product | None:
        products = self.load_products()
        for p in products:
            if p.name == name:
                return p
        return None
    
    def delete_product(self, name: str) -> bool:
        products = self.load_products()
        new_products = [p for p in products if p.name != name]

        if len(new_products) == len(products):
            return False

        self.save_products(new_products)
        return True
    
    def update_product(self, name: str, new_price: float) -> bool:
        products = self.load_products()
        updated = False

        for p in products:
            if p.name == name:
                p.price = new_price
                updated = True

        if updated:
            self.save_products(products)

        return updated