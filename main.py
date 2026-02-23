from pathlib import Path
from app.repositories.product_repository import ProductRepository
from app.services.user_services import UserService
from app.services.product_services import ProductService
from app.utils.helpers import format_price
from app.models.user import User
from app.models.product import Product
from app.errors.product_errors import ProductError

def main():
    repo = ProductRepository(Path("data/products.json"))
    p_service = ProductService(repo)
    #try:
    #    product = p_service.create_product("Plate", "Ceramic plate", 27, 45)
    #    product.price = format_price(product.price)
    #    #print(product)
    #except ProductError as e:
    #    print(f"Error: {e}")
    #p_service.update_price("Plate", 105)
    #print(p_service.list_products())
    #p_service.delete_product("Plate")
    #print(p_service.list_products())
    print(p_service.find_by_name("Glass"))

if __name__ == "__main__":
    main()