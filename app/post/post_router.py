from fastapi import APIRouter
from app.post.post_schema import PostCreate, Post
from app.post.post_service import PostService


class PostRouter:
    router = APIRouter()

    @router.get("/posts/", response_model=list[Post])
    def get_posts(skip: int = 0, limit: int = 100):
        post_service = PostService()
        db_posts = post_service.get_posts(skip=skip, limit=limit)
        return db_posts

    @router.post("/posts/", response_model=Post)
    def create_post(post: PostCreate):
        post_service = PostService()
        return post_service.create_post(post=post)

