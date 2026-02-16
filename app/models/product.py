from dataclasses import dataclass

@dataclass
class Product:
    name: str
    desc: str
    amount: int
    price: float

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.price < 0:
            raise ValueError("Price cannot be negative")