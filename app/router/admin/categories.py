from fastapi import APIRouter, Depends, status

from app.controller.CategoriesController import CategoriesController
from app.helper.response import ResponseModel, ListResponseModel
from app.model.Categories import CategoriesSchema
from app.router.auth.auth import TokenData
from app.router.auth.verify_token import get_current_user

router = APIRouter(
    prefix="/categories",
)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    summary="Get all categories",
    response_model=ListResponseModel,
)
async def get_all_categories(user: TokenData = Depends(get_current_user)):
    return await CategoriesController.get_all_categories()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Add new category",
    response_model=ResponseModel,
)
async def add_categories(
    request: CategoriesSchema, user: TokenData = Depends(get_current_user)
):
    return await CategoriesController.add_categories(request)


@router.put("/{category_id}", status_code=status.HTTP_200_OK, summary="Update category")
async def update_categories(
    category_id: str,
    request: CategoriesSchema,
    user: TokenData = Depends(get_current_user),
):
    return await CategoriesController.update_categories(category_id, request)


@router.delete(
    "/{category_id}", status_code=status.HTTP_200_OK, summary="Delete category"
)
async def delete_categories(
    category_id: str, user: TokenData = Depends(get_current_user)
):
    return await CategoriesController.delete_categories(category_id)
