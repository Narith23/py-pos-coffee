from datetime import datetime
from typing import Union
from bson import ObjectId
from pydantic import BaseModel, Field


class Categories(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the category",
        alias="_id",
    )
    name: str = Field(..., description="The name of the category")
    description: str = Field(..., description="The description of the category")
    created_at: datetime = Field(
        default=None,
        description="The date and time of creation of the category",
    )
    updated_at: datetime = Field(
        default=None, description="The date and time of last update of the category"
    )
    deleted_at: datetime = Field(
        default=None, description="The date and time of deletion of the category"
    )

    class Config:
        schema_extra = {
            "example": {
                "id": "some-id",
                "name": "Coffee",
                "description": "Coffee",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            },
            "allow_population_by_field_name": True,
        }


class ListCategories(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the category",
    )
    name: str = Field(..., description="The name of the category")
    description: str = Field(..., description="The description of the category")

    class Config:
        schema_extra = {
            "example": {
                "id": "some-id",
                "name": "Coffee",
                "description": "Coffee",
            },
            "allow_population_by_field_name": True,
        }


class CategoriesSchema(BaseModel):
    name: str
    description: Union[str, None] = None
