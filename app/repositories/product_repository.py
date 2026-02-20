import json
from pathlib import Path
from app.models.product import Product

DATA_PATH = Path("data/products.json")

class ProductRepository:

    def load_products(self) -> list[Product]:
        if not DATA_PATH.exists():
            return []

        with open(DATA_PATH, "r") as file:
            data = json.load(file)

        return [Product(**item) for item in data]

    def save_products(self, products: list[Product]) -> None:
        data = [product.__dict__ for product in products]

        with open(DATA_PATH, "w") as file:
            json.dump(data, file, indent=4)