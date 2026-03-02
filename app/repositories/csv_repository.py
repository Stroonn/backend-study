from datetime import date
import json
import csv
from pathlib import Path
from app.models.product import Product

#DATA_PATH = Path("data/products.json")

class ProductRepository_csv:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_products(self) -> list[Product]:
        if not self.file_path.exists():
            return []

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if self.file_path.suffix.lower() == ".csv":
            products = []
            with open(self.file_path, "r", newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    item = {
                        "id": int(row.get("id", 0)),
                        "name": row.get("name", ""),
                        "desc": row.get("desc", ""),
                        "amount": int(row.get("amount", 0)),
                        "price": float(row.get("price", 0)),
                        "created_at": row.get("created_at", ""),
                        "updated_at": row.get("updated_at", ""),
                    }
                    products.append(Product(**item))
            return products

        try:
            with open(self.file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
        except (json.JSONDecodeError, ValueError):
            return []

        return [Product(**item) for item in data]

    def save_products(self, products: list[Product]) -> None:

        # ensure parent directory exists
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = [product.__dict__ for product in products]

        # if target is CSV, write CSV; otherwise write JSON
        if self.file_path.suffix.lower() == ".csv":
            fieldnames = ["id", "name", "desc", "amount", "price", "created_at", "updated_at"]
            with open(self.file_path, "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for product in data:
                    writer.writerow({k: product.get(k, "") for k in fieldnames})
            return

        with open(self.file_path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def list_products(self) -> list[Product]:
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
                p.updated_at = str(date.today())
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
                p.updated_at = str(date.today())
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
                p.updated_at = str(date.today())
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
                p.updated_at = str(date.today())
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