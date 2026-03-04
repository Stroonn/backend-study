from pydantic import BaseModel

class ProductResponseSchema(BaseModel):
    id: int
    name: str
    desc: str
    amount: int
    price: float