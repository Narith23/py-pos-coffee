from datetime import datetime
from typing import Union
from bson import ObjectId
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Union[str] = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the user",
        alias="_id",
        primary_key=True,
        unique=True,
    )
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email of the user")
    password: str = Field(..., description="The password of the user")
    created_at: datetime = Field(
        default=None, description="The date and time of creation of the user"
    )
    updated_at: datetime = Field(
        default=None, description="The date and time of last update of the user"
    )
    deleted_at: datetime = Field(
        default=None, description="The date and time of deletion of the user"
    )

    class Config:
        schema_extra = {
            "example": {
                "_id": "some-id",
                "name": "John Doe",
                "email": "jdoe@me.com",
                "password": "password123",
                "created_at": "2022-01-01T00:00:00",
                "updated_at": "2022-01-01T00:00:00",
                "deleted_at": "2022-01-01T00:00:00",
            }
        }


class ListUsers(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="The ID of the user",
    )
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email of the user")

    class Config:
        schema_extra = {
            "example": {"id": "some-id", "name": "John Doe", "email": "jdoe@me.com"}
        }


class CreateUser(BaseModel):
    name: str
    email: str
    password: str
    
    
class UpdateUser(BaseModel):
    name: str
    email: str
    

class UpdatePassword(BaseModel):
    password: str
    new_password: str
    