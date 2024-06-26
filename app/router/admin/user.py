from fastapi import APIRouter, Depends, status

from app.controller.UserController import UserController
from app.model.Users import CreateUser, UpdatePassword, UpdateUser
from app.router.auth.auth import TokenData
from app.router.auth.verify_token import get_current_user

router = APIRouter(
    prefix="/user",
)


@router.get("", status_code=status.HTTP_200_OK, summary="Get all users")
async def get_all_users(user: TokenData = Depends(get_current_user)):
    return await UserController.get_all_users()


@router.post("", status_code=status.HTTP_201_CREATED, summary="Create new user")
async def create_user(request: CreateUser, user: TokenData = Depends(get_current_user)):
    return await UserController.add_users(request)


@router.put("/{user_id}", status_code=status.HTTP_200_OK, summary="Update user")
async def update_user(
    user_id: str, request: UpdateUser, user: TokenData = Depends(get_current_user)
):
    return await UserController.update_users(user_id, request)


@router.delete("/{user_id}", status_code=status.HTTP_200_OK, summary="Delete user")
async def delete_user(user_id: str, user: TokenData = Depends(get_current_user)):
    return await UserController.delete_users(user_id)


@router.put(
    "/{user_id}/password",
    status_code=status.HTTP_200_OK,
    summary="Update user password",
)
async def update_user_password(
    user_id: str, request: UpdatePassword, user: TokenData = Depends(get_current_user)
):
    return await UserController.update_user_password(user_id, request)
