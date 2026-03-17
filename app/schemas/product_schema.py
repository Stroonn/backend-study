from pydantic import BaseModel, Field, ConfigDict

class ProductCreateSchema(BaseModel):
    name: str = Field(min_length=1)
    desc: str
    amount: int = Field(gt=0)
    price: float = Field(gt=0)

class ProductResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    desc: str
    amount: int
    price: float