from fastapi import FastAPI,HTTPException, Depends
from pathlib import Path
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.services.product_services import ProductService
from app.schemas.product_schema import ProductResponseSchema, ProductCreateSchema
import sqlite3
from app.repositories.product_sql_repository import ProductSQLiteRepository


app = FastAPI()

def get_service():
    connection = sqlite3.connect("database.db", check_same_thread=False)
    repo = ProductSQLiteRepository(connection)
    return ProductService(repo)

@app.post("/products", response_model=ProductResponseSchema)
def create_product(payload: ProductCreateSchema,service: ProductService = Depends(get_service)):
    try:
        return service.create_product(
            name=payload.name,
            desc=payload.desc,
            amount=payload.amount,
            price=payload.price
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products", response_model=list[ProductResponseSchema])
def list_products(service: ProductService = Depends(get_service)):
    return service.list_products()

@app.get("/products/{name}", response_model=ProductResponseSchema)
def find_by_name(name: str, service: ProductService = Depends(get_service)):
    product = service.find_by_name(name)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.put("/products/{id}", response_model=ProductResponseSchema)
def update_name(id: int, new_name: str, service: ProductService = Depends(get_service)):

    updated_product = service.update_name(id, new_name)

    if updated_product:
        return updated_product

    raise HTTPException(status_code=404, detail="Product not found")
    
@app.delete("/products/{id}")
def delete_product(id: int, service: ProductService = Depends(get_service)):

    deleted = service.delete_product(id)

    if deleted:
        return {"message": "Product deleted successfully"}

    raise HTTPException(status_code=404, detail="Product not found")