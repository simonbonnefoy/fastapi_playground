from fastapi import APIRouter, HTTPException
from app.user.user_schema import User, UserCreate
from app.user.user_service import UserService


class UserRouter:
    router = APIRouter()

    def __init__(self): ...

    @router.post("/users/", response_model=User)
    def create_user(user: UserCreate):
        user_service = UserService()
        db_user = user_service.get_user_by_email(user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        db_user = user_service.create(user)
        return db_user

    @router.get("/users/", response_model=list[User])
    def read_users(skip: int = 0, limit: int = 100):
        user_service = UserService()
        users = user_service.get_users(skip=skip, limit=limit)
        return users
