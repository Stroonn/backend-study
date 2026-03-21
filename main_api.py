from fastapi import FastAPI,HTTPException, Depends, Request
from app.models.product import Product
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductResponseSchema, ProductCreateSchema
import sqlite3
from app.repositories.product_sql_repository import ProductSQLiteRepository
from app.database.database import get_connection, create_tables
import time
from app.core.logger import logger
from app.schemas.api_response import ApiResponse
from fastapi import Query
from app.errors.product_errors import ProductError

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000

    logger.info(
        f"{request.method} {request.url.path} | "
        f"Status: {response.status_code} | "
        f"{process_time:.2f}ms"
    )

    return response

def get_service():
    connection = get_connection()
    create_tables(connection)
    repo = ProductSQLiteRepository(connection)
    return ProductService(repo)

@app.post("/products", status_code=201, response_model=ProductResponseSchema)
def create_product(payload: ProductCreateSchema,service: ProductService = Depends(get_service)):
    try:
        return service.create_product(
            name=payload.name,
            desc=payload.desc,
            amount=payload.amount,
            price=payload.price
        )
    except ProductError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products")
def list_products(
    skip: int = 0,
    limit: int = 10,
    name: str | None = None,
    min_price: float | None = None,
    service: ProductService = Depends(get_service)
    ):

    products = service.list_products(skip, limit, name, min_price)

    return ApiResponse(
        success=True,
        data=products,
        pagination={
            "skip": skip,
            "limit": limit,
            "returned": len(products)
        }
    )

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