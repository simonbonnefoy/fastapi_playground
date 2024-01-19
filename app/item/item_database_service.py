from typing import Type

from app.item.item_model import ItemModel
from app.item.item_schema import ItemCreate, Item
from app.database_service.base_database_service import BaseDatabaseService
from app.database_service.database import DataBase

class ItemDatabaseService(BaseDatabaseService):
    database_session = DataBase().get_session()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Type[ItemModel]]:
        return self.database_session.query(ItemModel).offset(skip).limit(limit).all()

    def create(self, item: ItemCreate) -> Item:
        db_item = ItemModel(**item.dict())
        self.database_session.add(db_item)
        self.database_session.commit()
        self.database_session.refresh(db_item)
        return db_item

    def get_one_by_id(self, id: int) -> ItemModel:...
