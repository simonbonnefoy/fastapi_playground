from pydantic import BaseModel



class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: int | None = None


class ItemCreate(ItemBase):
    owner_id: int
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

