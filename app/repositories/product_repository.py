import json
from pathlib import Path
from app.models.product import Product

#DATA_PATH = Path("data/products.json")

class ProductRepository:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_products(self) -> list[Product]:
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r") as file:
            data = json.load(file)

        return [Product(**item) for item in data]

    def save_products(self, products: list[Product]) -> None:
        data = [product.__dict__ for product in products]

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
