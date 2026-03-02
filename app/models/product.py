from dataclasses import dataclass
from app.errors.product_errors import EmptyNameError, InvalidAmountError, InvalidPriceError

@dataclass
class Product:
    id : int
    name: str
    desc: str
    amount: int
    price: float
    created_at: str
    updated_at: str

    def __post_init__(self):
        if not self.name:
            raise EmptyNameError("Name cannot be empty")
        if self.amount <= 0:
            raise InvalidAmountError("Amount must be positive")
        if self.price < 0:
            raise InvalidPriceError("Price cannot be negative")