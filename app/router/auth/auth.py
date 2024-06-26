from datetime import datetime, timedelta
import logging
from fastapi import APIRouter, Depends, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import ExpiredSignatureError, JWTError, jwt

from app.helper.database import users
from app.helper.response import (
    BadRequestResponseModel,
    ErrorResponseModel,
    SuccessfulResponseModel,
    CreateResponseModel,
)

from app.helper.config import (
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
)
from app.helper.hash_pass import verify_password, hash_password


class RequestRegister(BaseModel):
    name: str
    email: str
    password: str


class TokenData(BaseModel):
    id: str
    name: str
    email: str


router = APIRouter()


async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=float(JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=float(JWT_REFRESH_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


# Auth Login and Register
@router.post("/login", status_code=status.HTTP_200_OK)
async def login(payload: OAuth2PasswordRequestForm = Depends()):
    user = await users.find_one({"email": payload.username})
    if not user:
        return {"msg": "Wrong username or password"}
    if not verify_password(payload.password, user["password"]):
        return {"msg": "Wrong username or password"}
    data = {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }
    token = {
        "access_token": await create_access_token(data),
        "refresh_token": await create_refresh_token(data),
    }
    return SuccessfulResponseModel(result=token)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(payload: RequestRegister):
    # validation user
    user = await users.find_one({"email": payload.email})
    if user:
        return BadRequestResponseModel(result="User already exists")
    user = await users.insert_one(
        {
            "name": payload.name,
            "email": payload.email,
            "password": hash_password(payload.password),
        }
    )
    await users.update_one(
        {"_id": user.inserted_id}, {"$currentDate": {"created_at": True}}
    )
    return CreateResponseModel(message="User created successfully")


@router.post("/refresh", status_code=status.HTTP_200_OK)
async def refresh(refresh_token: str = Form(...)):
    try:
        payload = jwt.decode(refresh_token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        data = {
            "id": str(payload["id"]),
            "name": payload["name"],
            "email": payload["email"],
        }
        token = {
            "access_token": await create_access_token(data),
            "refresh_token": await create_refresh_token(data),
        }
        return SuccessfulResponseModel(result=token)
    except ExpiredSignatureError:
            logging.exception("The refresh token has expired.")
            return BadRequestResponseModel(message="The refresh token has expired.")
    except JWTError as e:
        logging.exception(f"{str(e)}")
        return ErrorResponseModel()

@router.get("/logout", status_code=status.HTTP_200_OK)
async def logout():
    pass


@router.post("/login/swagger", status_code=status.HTTP_200_OK)
async def login_swagger(payload: OAuth2PasswordRequestForm = Depends()):
    user = await users.find_one({"email": payload.username})
    if not user:
        return {"msg": "Wrong username or password"}
    if not verify_password(payload.password, user["password"]):
        return {"msg": "Wrong username or password"}
    data = {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }
    token = {
        "access_token": await create_access_token(data),
        "refresh_token": await create_refresh_token(data),
    }
    return token
