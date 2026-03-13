from app.models.product import Product
from app.utils.helpers import calculate_discount, is_positive, format_price
from datetime import date

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name, desc, amount, price):
        if not name.strip():
            raise ValueError("Nome obrigatório")
        
        if len(name) < 3:
            raise ValueError("Nome deve conter pelo mais de 3 caracteres")

        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")
        
        if amount > 1000:
            raise ValueError("Quantidade muito alta")

        if price <= 0:
            raise ValueError("Preço deve ser positivo")
        
        if price > 10000:
            raise ValueError("Preço muito alto")

        return self.repository.create_product(
                name=name,
                desc=desc,
                amount=amount,
                price=price
            )
    
    def list_products(self):
        return self.repository.list_products()
    
    def find_by_name(self, name):
        return self.repository.find_by_name(name)
    
    def find_by_price_less_than(self, price):
        if price <= 0:
            raise ValueError("Preço inválido")
        return self.repository.find_by_price_less_than(price)
    
    def find_by_amount_greater_than(self, amount):
        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")
        return self.repository.find_by_amount_greater_than(amount)
    
    def order_by_price(self, ascending=True):
        return self.repository.order_by_price(ascending)
    
    def order_by_price_descending(self):
        return self.repository.order_by_price(ascending=False)
    
    def update_name(self, id: int, new_name: str):

        self.repository.update_name(id, new_name)

        product = self.repository.find_by_id(id)

        return product
    
    def update_description(self, id, desc):
        if not desc.strip():
            raise ValueError("Descrição obrigatória")
        return self.repository.update_desc(id, desc)
    
    def update_amount(self, id, amount):
        if amount <= 0:
            raise ValueError("Quantidade deve ser positiva")
        elif amount > 1000:
            raise ValueError("Quantidade muito alta")
        return self.repository.update_amount(id, amount)

    def update_price(self, id, price):
        if price <= 0:
            raise ValueError("Preço inválido")
        elif price > 10000:
            raise ValueError("Preço muito alto")
        return self.repository.update_price(id, price)
    
    def delete_product(self, id: int):

        product = self.repository.find_by_id(id)

        if not product:
            return None

        self.repository.delete_product(id)

        return True