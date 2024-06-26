from bson import ObjectId
from fastapi import Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.helper.database import products, categories
from app.helper.response import (
    BadRequestResponseModel,
    CreateResponseModel,
    SuccessfulResponseModel,
)
from app.model.Product import ListProducts, Product, ProductSchemaCreate
from app.router.auth.auth import TokenData


product_templates = Jinja2Templates(directory="templates/admin/product")


class ProductController:
    @staticmethod
    async def get_all_products():
        cursor = await products.find({"deleted_at": None}).to_list(length=100)
        return SuccessfulResponseModel(
            result=[ListProducts(**data, id=str(data["_id"])) for data in cursor]
        )

    @staticmethod
    async def add_products(request: ProductSchemaCreate):
        # validation category_id
        category = await categories.find_one({"_id": request.category_id})
        if not category:
            return BadRequestResponseModel(message="Category not found")
        # create product
        product = Product(
            name=request.name,
            description=request.description,
            price=request.price,
            qty=request.qty,
            category_id=request.category_id,
        )
        data = await products.insert_one(product.dict(by_alias=True))
        await products.update_one(
            {"_id": data.inserted_id}, {"$currentDate": {"created_at": True}}
        )
        return CreateResponseModel()

    @staticmethod
    async def update_products(product_id: str, request: Product):
        # validation category_id
        category = await categories.find_one({"_id": request.category_id})
        if not category:
            return BadRequestResponseModel(message="Category not found")
        await products.update_one(
            {"_id": str(ObjectId(product_id))},
            {"$set": request.dict(by_alias=True), "$currentDate": {"updated_at": True}},
        )
        return SuccessfulResponseModel()

    @staticmethod
    async def delete_products(product_id: str):
        await products.update_one(
            {"_id": str(ObjectId(product_id))}, {"$currentDate": {"deleted_at": True}}
        )
        return SuccessfulResponseModel()

    @staticmethod
    async def get_all_products_web(user: TokenData):
        pipeline = [
            {"$match": {"deleted_at": None}},
            {
                "$lookup": {
                    "from": "categories",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category",
                }
            },
            {"$unwind": "$category"},
        ]
        cursor = await products.aggregate(pipeline).to_list(length=100)
        return product_templates.TemplateResponse(
            "index.html", {"request": user, "cursor": cursor}
        )

    @staticmethod
    async def create_product_web(user: TokenData):
        category = await categories.find({"deleted_at": None}).to_list(length=100)
        return product_templates.TemplateResponse(
            "create.html", {"request": user, "category": category}
        )

    @staticmethod
    async def add_products_web(request: Request, payload: ProductSchemaCreate, user: TokenData):
        # validation category_id
        category = await categories.find_one(
            {"_id": payload.category_id, "deleted_at": None}
        )
        if not category:
            category = await categories.find({"deleted_at": None}).to_list(length=100)
            return product_templates.TemplateResponse(
                "create.html",
                {"request": user, "category": category, "error": "Category not found"},
            )
        # create product
        product = Product(
            name=payload.name,
            description=payload.description,
            price=payload.price,
            qty=payload.qty,
            category_id=payload.category_id,
        )
        data = await products.insert_one(product.dict(by_alias=True))
        await products.update_one(
            {"_id": data.inserted_id}, {"$currentDate": {"created_at": True}}
        )
        
        return SuccessfulResponseModel(
            message="Product added successfully",
        )