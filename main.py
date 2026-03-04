from pathlib import Path
## import para o JSON como arquivo de dados
from app.repositories.product_repository import ProductRepository
##import para usar o csv como arquivo de dados
#from app.repositories.csv_repository import ProductRepository_csv
from app.services.user_services import UserService
from app.services.product_services import ProductService
from app.utils.helpers import format_price
from app.models.user import User
from app.models.product import Product
from app.errors.product_errors import ProductError

def main():
    ##caminho usando o csv como arquivo de dados
    #repo = ProductRepository_csv(Path("data/products.csv"))

    ##caminho usando o json como arquivo de dados
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
    #print(p_service.find_by_name("Glass"))

    while True:
        print("\nMenu:")
        print("\n 1. Criar produto")
        print("\n 2. Listar produtos")
        print("\n 3. Buscar produto")
        print("\n 4. Atualizar produto")
        print("\n 5. Deletar produto")
        print("\n 0. Sair")
        choice = int(input("Escolha uma opção: "))

        if choice == 1:
            print("Digite o ID do produto:")
            id = int(input())
            print("Digite o nome do produto:")
            name = input()
            print("Digite a descrição do produto:")
            description = input()
            print("Digite a quantidade do produto:")
            amount = int(input())
            print("Digite o preço do produto:")
            price = float(input())
            try:
                p_service.create_product(id, name, description, amount, price)
            except ProductError as e:
                print(f"Error: {e}")
        elif choice == 2:
            print(p_service.list_products())
        elif choice == 3:
            print("\n 1. Buscar produto por nome")
            print("\n 2. Buscar produto por preço menor que x")
            print("\n 3. Buscar produto por quantidade maior que x")
            print("\n 4. Ordenar produtos por preço")
            sub_choice = int(input("Escolha uma opção: "))
            if sub_choice == 1:
                print("Digite o nome do produto:")
                name = input()
                print(p_service.find_by_name(name))
            elif sub_choice == 2:
                print("Digite o preço limite:")
                price = float(input())
                try:
                    print(p_service.find_by_price_less_than(price))
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == 3:
                print("Digite a quantidade limite:")
                amount = int(input())
                try:
                    print(p_service.find_by_amount_greater_than(amount))
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == 4:
                print("1. Ordenar do menor para o maior")
                print("2. Ordenar do maior para o menor")
                order_choice = int(input("Escolha uma opção: "))
                if order_choice == "1":
                    print(p_service.order_by_price(ascending=True))
                elif order_choice == "2":
                    print(p_service.order_by_price_descending())
                else:
                    print("Opção inválida.")
        elif choice == 4:
            print("\n 1. Atualizar o nome")
            print("\n 2. Atualizar a descrição do produto")
            print("\n 3. Atualizar a quantidade do produto")
            print("\n 4. Atualizar o preço do produto")
            sub_choice = int(input("Escolha uma opção: "))
            if sub_choice == 1:
                print("Digite o ID do produto:")
                id = int(input())
                print("Digite o novo nome do produto:")
                name = input()
                try:
                    p_service.update_name(id, name)
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == 2:
                print("Digite o ID do produto:")
                id = int(input())
                print("Digite a nova descrição do produto:")
                desc = input()
                try:
                    p_service.update_description(id, desc)
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == 3:
                print("Digite o ID do produto:")
                id = int(input())
                print("Digite a nova quantidade do produto:")
                amount = int(input())
                try:
                    p_service.update_amount(id, amount)
                except ValueError as e:
                    print(f"Error: {e}")
            elif sub_choice == 4:
                print("Digite o ID do produto:")
                id = int(input())
                print("Digite o novo preço do produto:")
                price = float(input())
                try:
                    p_service.update_price(id, price)
                except ValueError as e:
                    print(f"Error: {e}")
        
        elif choice == 5:
            print("Digite o ID do produto a ser deletado:")
            id = int(input())
            if p_service.delete_product(id):
                print("Produto deletado com sucesso!")
            else:
                print("Produto não encontrado.")
        
        elif choice == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()