from fastapi import FastAPI
from pathlib import Path
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.services.product_services import ProductService
from app.schemas.product_schema import ProductCreateSchema


app = FastAPI()

repo = ProductRepository(Path("data/products.json"))
service = ProductService(repo)

@app.post("/api/product")
def create_product(payload: ProductCreateSchema):
    try:
        # Transformamos o Schema em dicionário e passamos os argumentos soltos
        # Isso vai encaixar perfeitamente na sua função original:
        # create_product(id, name, desc, amount, price)
        return service.create_product(
            id=payload.id,
            name=payload.name,
            desc=payload.desc,
            amount=payload.amount,
            price=payload.price
        )
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/list_products")
def list_products():
    return {"products": service.list_products()}

@app.get("/api/find_by_name")
def find_by_name(name: str):
    product = service.find_by_name(name)
    if product:
        return product
    else:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.put("/api/update_name")
def update_name(id: int, new_name: str):
    try:
        updated_product = service.update_name(id, new_name)
        if updated_product:
            return updated_product
        else:
            from fastapi import HTTPException
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))
    
@app.delete("/api/delete_product")
def delete_product(id: int):
    try:
        service.delete_product(id)
        return {"message": "Product deleted successfully"}
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(e))