class Product:

    def __init__(self, name:str, desc:str, amount:int, price:int):
        if price <= 0:
            raise ValueError("Price must be positive!")
        if not name:
            raise ValueError("Name cannot be empty")
        if not desc:
            raise ValueError("Desc cannot be empty")
        if not amount:
            raise ValueError("Amount must be positive!")
        
        self.name = name
        self.desc = desc
        self.amount = amount
        self.price = price

###usar aspas tripla ou repetir f"contudo , \n"
    def __repr__(self):
        return f"""Product(name = {self.name},
        description = {self.desc}, 
        amount = {self.amount},
        price = {self.price})"""