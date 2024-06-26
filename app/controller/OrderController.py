from app.helper.database import orders
from app.helper.response import SuccessfulResponseModel
from app.model.Orders import ListOrders


class OrderController:
    @staticmethod
    async def get_all_orders():
        cursor = await orders.find({"deleted_at": None}).to_list(length=100)
        return SuccessfulResponseModel(
            result=[ListOrders(**data, id=str(data["_id"])) for data in cursor]
        )
