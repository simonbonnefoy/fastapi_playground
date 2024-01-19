from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database_service.database import Base


class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    writer = relationship("UserModel", back_populates="post")

