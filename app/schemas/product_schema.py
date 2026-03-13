from pydantic import BaseModel, Field

class ProductCreateSchema(BaseModel):
    name: str
    desc: str
    amount: int = Field(ge=0)
    price: float = Field(gt=0)

class ProductResponseSchema(BaseModel):
    id: int
    name: str
    desc: str
    amount: int
    price: float