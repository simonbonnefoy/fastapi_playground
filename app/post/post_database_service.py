from sqlalchemy.orm import Session

from app.post.post_schema import PostCreate
from app.post.post_model import PostModel
from app.database_service.base_database_service import BaseDatabaseService
from app.database_service.database import DataBase


class PostDatabaseService(BaseDatabaseService[PostCreate, PostModel]):
    database_session: Session = DataBase().get_session()

    def get_all(self, skip: int = 0, limit: int = 100) -> list[PostModel] | None:
        db_posts = self.database_session.query(PostModel).offset(skip).limit(limit).all()
        return db_posts

    def get_one_by_id(self, id: int) -> PostModel:
        db_post = self.database_session.query(PostModel).filter(PostModel.id == id).first()
        return db_post

    def create(self, post: PostCreate) -> PostModel:
        db_post = PostModel(**post.dict())
        self.database_session.add(db_post)
        self.database_session.commit()
        self.database_session.refresh(db_post)
        return db_post

    def delete_one(self): ...

    def update_one(self): ...
