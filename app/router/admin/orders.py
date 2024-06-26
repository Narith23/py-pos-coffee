from fastapi import APIRouter, Depends, status

from app.controller.OrderController import OrderController
from app.router.auth.auth import TokenData
from app.router.auth.verify_token import get_current_user

router = APIRouter(
    prefix="/orders",
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_all_orders(user: TokenData = Depends(get_current_user)):
    return await OrderController.get_all_orders()
