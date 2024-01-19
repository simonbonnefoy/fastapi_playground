from typing import Type

from app.user.user_model import UserModel
from app.user.user_schema import UserCreate, User
from app.database_service.base_database_service import BaseDatabaseService
from app.database_service.database import DataBase


class UserDatabaseService(BaseDatabaseService[User, UserCreate]):
    database_session = DataBase().get_session()


    def create(self, user: UserCreate) -> User:
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = UserModel(email=user.email, hashed_password=fake_hashed_password)
        self.database_session.add(db_user)
        self.database_session.commit()
        self.database_session.refresh(db_user)
        return db_user

    def get_one_by_email(self, email: str) -> User:
        return self.database_session.query(UserModel).filter(UserModel.email == email).first()

    def get_one_by_id(self, id: int) -> User:
        return self.database_session.query(UserModel).filter(UserModel.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Type[UserModel]]:
        return self.database_session.query(UserModel).offset(skip).limit(limit).all()
