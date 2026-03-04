from pydantic import BaseModel

class ProductCreateSchema(BaseModel):
    id: int
    name: str
    desc: str
    amount: int
    price: float