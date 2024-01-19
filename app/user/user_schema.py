from pydantic import BaseModel
from app.item.item_schema import Item

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []
    hashed_password: str

    class Config:
        orm_mode = True
