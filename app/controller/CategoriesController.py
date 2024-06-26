from datetime import datetime
from typing import List
from bson import ObjectId
from app.helper.response import (
    CreateResponseModel,
    ListResponseModel,
    SuccessfulResponseModel,
)
from app.model.Categories import Categories, CategoriesSchema, ListCategories

from app.helper.database import categories


class CategoriesController:
    @staticmethod
    async def get_all_categories():
        cursor = await categories.find({"deleted_at": None}).to_list(length=100)
        return SuccessfulResponseModel(
            result=[ListCategories(**data, id=str(data["_id"])) for data in cursor]
        )

    @staticmethod
    async def add_categories(request: CategoriesSchema):
        category = Categories(name=request.name, description=request.description)
        data = await categories.insert_one(category.dict(by_alias=True))
        await categories.update_one(
            {"_id": data.inserted_id}, {"$currentDate": {"created_at": True}}
        )
        return CreateResponseModel()

    @staticmethod
    async def update_categories(category_id: str, request: CategoriesSchema):
        await categories.update_one(
            {"_id": str(ObjectId(category_id))},
            {"$set": request.dict(by_alias=True), "$currentDate": {"updated_at": True}},
        )
        return SuccessfulResponseModel()

    @staticmethod
    async def delete_categories(category_id: str):
        await categories.update_one(
            {"_id": str(ObjectId(category_id))}, {"$currentDate": {"deleted_at": True}}
        )
        return SuccessfulResponseModel()
