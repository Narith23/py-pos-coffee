from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field


class OrderItems(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the order",
        alias="_id",
    )
    order_id: str = Field(
        description="The ID of the order",
    )
    product_id: str = Field(
        description="The ID of the product",
    )
    qty: int = Field(
        description="The quantity of the product",
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
                "order_id": "some-id",
                "product_id": "some-id",
                "qty": 0,
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }


class ListOrderItems(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the order",
        alias="_id",
    )
    order_id: str = Field(
        description="The ID of the order",
    )
    product_id: str = Field(
        description="The ID of the product",
    )
    qty: int = Field(
        description="The quantity of the product",
    )
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the order"
    )

    class Config:
        schema_extra = {
            "example": {
                "_id": "some-id",
                "order_id": "some-id",
                "product_id": "some-id",
                "qty": 0,
                "created_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }


class CreateOrderItems(BaseModel):
    order_id: str = Field(
        description="The ID of the order",
    )
    product_id: str = Field(
        description="The ID of the product",
    )
    qty: int = Field(
        description="The quantity of the product",
    )

    class Config:
        schema_extra = {
            "example": {
                "order_id": "some-id",
                "product_id": "some-id",
                "qty": 0,
            },
            "allow_population_by_field_name": True,
        }


class UpdateOrderItems(BaseModel):
    qty: int = Field(
        description="The quantity of the product",
    )

    class Config:
        schema_extra = {
            "example": {
                "qty": 0,
            },
            "allow_population_by_field_name": True,
        }
