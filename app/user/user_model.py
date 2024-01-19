from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database_service.database import Base

# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#     from app.models.item import ItemModel
#     from app.models.post import PostModel

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("ItemModel", back_populates="owner")
    post = relationship(argument="PostModel", back_populates="writer")
