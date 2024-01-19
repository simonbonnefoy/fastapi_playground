from app.post.post_database_service import PostDatabaseService
from app.post.post_model import PostModel
from app.post.post_schema import PostCreate, Post


class PostService:

    def __init__(self):
        self.crud = PostDatabaseService()

    def get_posts(self, skip: int=0, limit: int=0) -> list[PostModel] | None:
        db_posts = self.crud.get_all(skip=skip, limit=limit)
        return db_posts

    def create_post(self, post: PostCreate) -> Post:
        db_post = self.crud.create(post=post)
        return db_post

