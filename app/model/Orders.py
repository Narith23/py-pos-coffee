from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field


class Orders(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the order",
        alias="_id",
    )
    user_id: str = Field(
        description="The ID of the user",
        foreign_key="users.id",
    )
    total_amount: float = Field(
        description="The total amount of the order",
    )
    status_order: str = Field(
        description="The status of the order",
    )
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the order"
    )
    updated_at: datetime = Field(
        default=None, description="The date and time of last update of the order"
    )
    deleted_at: datetime = Field(
        default=None, description="The date and time of deletion of the order"
    )

    class Config:
        schema_extra = {
            "example": {
                "_id": "some-id",
                "user_id": "some-id",
                "total_amount": 0.0,
                "status_order": "pending",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }


class ListOrders(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the order",
    )
    user_id: str = Field(
        description="The ID of the user",
    )
    total_amount: float = Field(
        description="The total amount of the order",
    )
    status_order: str = Field(
        description="The status of the order",
    )
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the order"
    )


class CreateOrder(BaseModel):
    user_id: str = Field(
        description="The ID of the user",
    )
    total_amount: float = Field(
        description="The total amount of the order",
    )
    status_order: str = Field(
        description="The status of the order",
    )


class UpdateOrder(BaseModel):
    total_amount: float = Field(
        description="The total amount of the order",
    )
    status_order: str = Field(
        description="The status of the order",
    )
