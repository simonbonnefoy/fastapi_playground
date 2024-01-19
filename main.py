from fastapi import FastAPI
import uvicorn
from app.user.user_router import UserRouter
from app.item.item_router import ItemRouter
from app.post.post_router import PostRouter

from app.database_service.database import engine
from app.database_service.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(UserRouter.router)
app.include_router(ItemRouter.router)
app.include_router(PostRouter.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
