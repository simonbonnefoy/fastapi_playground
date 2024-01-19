from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")
U = TypeVar("U")


class BaseDatabaseService(ABC, Generic[T, U]):

    @abstractmethod
    def get_all(self, skip: int =0, limit: int =100) -> list[U]:
        ...

    @abstractmethod
    def create(self, entry: T) -> U:
        ...

    @abstractmethod
    def get_one_by_id(self, id: int) -> U:
        ...

    #
    # @abstractmethod
    # def delete_one(self, session: Session):...
    #
    # @abstractmethod
    # def update_one(self, session: Session):...
