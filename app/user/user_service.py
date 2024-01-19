from typing import Type

from app.user.user_model import UserModel
from app.user.user_database_service import UserDatabaseService
from app.user.user_schema import UserCreate, User


class UserService:

    def __init__(self):
        self.crud = UserDatabaseService()

    def create(self, user: UserCreate) -> User:
        db_user = self.crud.create(user=user)
        return db_user

    def get_users(self, skip: int = 0, limit: int = 100) -> list[Type[UserModel]]:
        db_users = self.crud.get_all(skip=skip, limit=limit)
        return db_users

    def get_user_by_email(self, email: str) -> User:
        db_user = self.crud.get_one_by_email(email=email)
        return db_user
