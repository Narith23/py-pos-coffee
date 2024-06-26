from fastapi import APIRouter, Depends, Form, Request, status

from app.controller.ProductController import ProductController
from app.model.Product import ProductSchemaCreate, ProductSchemaUpdate
from app.router.auth.auth import TokenData
from app.router.auth.verify_token import get_current_user, get_web_user

router = APIRouter(
    prefix="/products",
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_products(user: TokenData = Depends(get_current_user)):
    return await ProductController.get_all_products()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_product(
    request: ProductSchemaCreate, user: TokenData = Depends(get_current_user)
):
    return await ProductController.add_products(request)


@router.put("/{product_id}", status_code=status.HTTP_200_OK)
async def update_product(
    product_id: str,
    request: ProductSchemaUpdate,
    user: TokenData = Depends(get_current_user),
):
    return await ProductController.update_products(product_id, request)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(product_id: str, user: TokenData = Depends(get_current_user)):
    return await ProductController.delete_products(product_id)


@router.get("/web", status_code=status.HTTP_200_OK)
async def get_all_products_web(user: TokenData = Depends(get_web_user)):
    return await ProductController.get_all_products_web(user)

@router.get("/web/create", status_code=status.HTTP_200_OK)
async def create_product_web(user: TokenData = Depends(get_web_user)):
    return await ProductController.create_product_web(user)

@router.post("/web/create", status_code=status.HTTP_201_CREATED)
async def add_products_web(request: Request, payload: ProductSchemaCreate, user: TokenData = Depends(get_web_user)):
    return await ProductController.add_products_web(request, payload, user)
