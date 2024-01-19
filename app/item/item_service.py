from typing import Type
from app.item.item_model import ItemModel
from app.item.item_database_service import ItemDatabaseService
from app.item.item_schema import ItemCreate, Item


class ItemService:

    def __init__(self):
        self.crud = ItemDatabaseService()

    def get_items(self, skip: int = 0, limit: int = 100) -> list[Type[ItemModel]]:
        return self.crud.get_all(skip=skip, limit=limit)

    def create(self, item: ItemCreate) -> Item:
        db_item = self.crud.create(item)
        return db_item
