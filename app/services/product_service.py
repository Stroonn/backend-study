from app.models.product import Product
from app.core.logger import logger

class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def create_product(self, name, desc, amount, price):

        logger.info(f"Attempting to create product: {name}")

        if not name.strip():
            logger.warning("Product creation failed: empty name")
            raise ValueError("Name can't be empty")
            
        if len(name) < 3:
            logger.warning("Product creation failed: name too short")
            raise ValueError("Name must be at least 3 characters long")

        if amount <= 0:
            logger.warning("Product creation failed: invalid amount")
            raise ValueError("Amount must be positive")
            
        if amount > 1000:
            logger.warning("Product creation failed: amount too high")
            raise ValueError("Amount too high")

        if price <= 0:
            logger.warning("Product creation failed: invalid price")
            raise ValueError("Price must be positive")
            
        if price > 10000:
            logger.warning("Product creation failed: price too high")
            raise ValueError("Price too high")

        product = self.repository.create_product(
            name=name,
            desc=desc,
            amount=amount,
            price=price
        )

        logger.info(f"Product created successfully: {name}")

        return product

    def list_products(self, skip: int, limit: int, name=None, min_price=None):

        logger.info(
            f"Listing products skip={skip} limit={limit} name={name} min_price={min_price}"
        )

        return self.repository.list_products(skip, limit, name, min_price)
    
    def find_by_name(self, name):
        return self.repository.find_by_name(name)
    
    def update_name(self, id: int, new_name: str):

        logger.info(f"Updating product name: id={id} new_name={new_name}")

        product = self.repository.find_by_id(id)

        if not product:
            logger.warning(f"Update failed: product id={id} not found")
            return None

        self.repository.update_name(id, new_name)

        return self.repository.find_by_id(id)
    
    def update_description(self, id, desc):
        if not desc.strip():
            raise ValueError("Description necessary")
        return self.repository.update_desc(id, desc)
    
    def update_amount(self, id, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        elif amount > 1000:
            raise ValueError("Amount too high")
        return self.repository.update_amount(id, amount)

    def update_price(self, id, price):
        if price <= 0:
            raise ValueError("Wrong price")
        elif price > 10000:
            raise ValueError("Price too high")
        return self.repository.update_price(id, price)
    
    def delete_product(self, id: int):

        logger.info(f"Attempting to delete product id={id}")

        deleted = self.repository.delete_product(id)
        if not deleted:
            logger.warning(f"Delete failed: product id={id} not found")
            return None

        logger.info(f"Product deleted successfully: id={id}")
        
        return True