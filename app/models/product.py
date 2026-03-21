from dataclasses import dataclass
from app.errors.product_errors import EmptyNameError, InvalidAmountError, InvalidPriceError

@dataclass
class Product:
    id : int
    name: str
    desc: str
    amount: int
    price: float
