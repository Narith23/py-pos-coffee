from bson import ObjectId
from app.helper.hash_pass import hash_password, verify_password
from app.helper.response import (
    BadRequestResponseModel,
    CreateResponseModel,
    SuccessfulResponseModel,
)
from app.helper.database import users
from app.model.Users import CreateUser, ListUsers, UpdatePassword, UpdateUser, User


class UserController:
    @staticmethod
    async def get_all_users():
        cursor = await users.find({"deleted_at": None}).to_list(length=100)
        return SuccessfulResponseModel(
            result=[ListUsers(**data, id=str(data["_id"])) for data in cursor]
        )

    @staticmethod
    async def add_users(request: CreateUser):
        request.password = hash_password(request.password)
        user = User(name=request.name, email=request.email, password=request.password)
        data = await users.insert_one(user.dict(by_alias=True))
        await users.update_one(
            {"_id": data.inserted_id}, {"$currentDate": {"created_at": True}}
        )
        return CreateResponseModel()

    @staticmethod
    async def update_users(user_id: str, request: UpdateUser):
        await users.update_one(
            {"_id": str(ObjectId(user_id))},
            {"$set": request.dict(by_alias=True), "$currentDate": {"updated_at": True}},
        )
        return SuccessfulResponseModel()

    @staticmethod
    async def delete_users(user_id: str):
        await users.update_one(
            {"_id": str(ObjectId(user_id))}, {"$currentDate": {"deleted_at": True}}
        )
        return SuccessfulResponseModel()
    
    
    @staticmethod
    async def update_user_password(user_id: str, request: UpdatePassword):
        user = await users.find_one({"_id": str(ObjectId(user_id))})
        if not verify_password(request.password, user["password"]):
            return BadRequestResponseModel(
                message="Wrong password"
            )
        await users.update_one(
            {"_id": str(ObjectId(user_id))},
            {"$set": {"password": hash_password(request.new_password), "$currentDate": {"updated_at": True}}},
        )
        return SuccessfulResponseModel()
