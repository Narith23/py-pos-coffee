from fastapi import APIRouter, status

from app.controller.ProductController import ProductController
from app.model.Product import ProductSchemaCreate, ProductSchemaUpdate

router = APIRouter(
    prefix="/products",
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_products():
    return await ProductController.get_all_products()

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(request: ProductSchemaCreate):
    return await ProductController.add_products(request)

@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(product_id: str, request: ProductSchemaUpdate):
    return await ProductController.update_products(product_id, request)

@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: str):
    return await ProductController.delete_products(product_id)
