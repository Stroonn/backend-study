class FakeRepository:
    def __init__(self):
        self.products = []

    def load_products(self):
        return self.products

    def save_products(self, products):
        self.products = products

    def list_products(self):
        return self.load_products()

    def delete_product(self, name: str) -> bool:
        original_count = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        return len(self.products) < original_count

    def update_product(self, name: str, new_price: float) -> bool:
        updated = False
        for p in self.products:
            if p.name == name:
                p.price = new_price
                updated = True
        return updated

    def find_by_name(self, name: str):
        for p in self.products:
            if p.name == name:
                return p
        return None