from app.services.user_services import UserService
from app.services.product_services import ProductService

def main():
    service = UserService()
    user = service.create_user("Matheus", "matheus@gmail.com")
    print(user)

    p_service = ProductService()
    try:
        product = p_service.create_product("Glass", "Blue glass", 10, 50)
    except ValueError as e:
        print(f"Error: {e}")
    print(product)
    
if __name__ == "__main__":
    main()