from app.services.user_services import UserService
from app.services.product_services import ProductService
from app.utils.helpers import format_price
from app.models.user import User
from app.models.product import Product
from app.errors.product_errors import ProductError

def main():
    #service = UserService()
    #u1 = service.create_user("Matheus", "matheus@gmail.com")
    #print(u1)
    #u2 =  service.create_user("Gabriela", "gabriela@gmail.com")
    
    p_service = ProductService()
    try:
        product = p_service.create_product("Glass", "Blue glass", 10, -50)
    except ProductError as e:
        print(f"Error: {e}")
    product.price = format_price(product.price)
    print(product)

    #u1 = User("Matheus", "matheus@gmail.com")
    #u2 = User("Matheus", "matheus@gmail.com")

    #print(u1 == u2)

    #p1 = Product("Glass", "Blue glass", 10, 50)
    #p1.price = format_price(p1.price)
    #print(p1)

if __name__ == "__main__":
    main()