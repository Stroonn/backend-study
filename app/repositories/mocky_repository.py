class FakeRepository:
    def __init__(self):
        self.products = []

    def load_products(self):
        return self.products

    def save_products(self, products):
        self.products = products