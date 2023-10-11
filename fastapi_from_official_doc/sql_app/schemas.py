from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: int | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
