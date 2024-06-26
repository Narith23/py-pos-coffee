from datetime import datetime
from typing import Union
from bson import ObjectId
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the product",
        alias="_id",
    )
    name: str = Field(..., description="The name of the product")
    description: Union[str, None] = Field(default=None, description="The description of the product")
    price: float = Field(default=0.0, description="The price of the product")
    qty: int = Field(default=0, description="The quantity of the product")
    category_id: str = Field(
        ..., description="The ID of the parent category", foreign_key="categories.id"
    )
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the product"
    )
    updated_at: datetime = Field(
        default=None, description="The date and time of last update of the product"
    )
    deleted_at: datetime = Field(
        default=None, description="The date and time of deletion of the product"
    )

    class Config:
        schema_extra = {
            "example": {
                "id": "some-id",
                "name": "Coffee",
                "description": "Coffee",
                "price": 0.0,
                "qty": 0,
                "category_id": "some-id",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }


class ListProducts(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the product",
        # alias="_id",
    )
    name: str = Field(..., description="The name of the product")
    description: Union[str, None] = Field(..., description="The description of the product")
    price: float = Field(default=0.0, description="The price of the product")
    qty: int = Field(default=0, description="The quantity of the product")
    category_id: str = Field(
        ..., description="The ID of the parent category", foreign_key="categories.id"
    )


class ProductSchemaCreate(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    qty: int
    category_id: str


class ProductSchemaUpdate(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    qty: int
    category_id: str
