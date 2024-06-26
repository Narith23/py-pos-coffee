from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field


class Payments(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the payment",
        alias="_id",
    )
    order_id: str = Field(
        description="The ID of the order",
    )
    amount: float = Field(
        description="The amount of the payment",
    )
    status_payment: str = Field(
        description="The status of the payment",
    )
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the payment"
    )
    updated_at: datetime = Field(
        default=None, description="The date and time of last update of the payment"
    )
    deleted_at: datetime = Field(
        default=None, description="The date and time of deletion of the payment"
    )

    class Config:
        schema_extra = {
            "example": {
                "_id": "some-id",
                "order_id": "some-id",
                "amount": 0.0,
                "status_payment": "pending",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }
