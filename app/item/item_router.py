from fastapi import APIRouter
from app.item.item_schema import Item, ItemCreate
from app.item.item_service import ItemService


class ItemRouter:
    router = APIRouter()

    @router.get("/items/", response_model=list[Item])
    def get_items(skip: int = 0, limit: int = 100):
        items_service = ItemService()
        items = items_service.get_items(skip=skip, limit=limit)
        return items

    @router.post("/items/", response_model=Item)
    def create_item(item: ItemCreate):
        items_service = ItemService()
        items = items_service.create(item=item)
        return items

