from fastapi import FastAPI
from fastapi_test.services.database.api import DBApi
from fastapi_test.services.database.tables.models import User, Post
from fastapi_test.services.database.schemas import UserSchema
from typing import Optional
import uvicorn

database = DBApi(f"sqlite:///test_sqlite.db")
# database.create_all_tables()
# user1 = User('user1', 'password', 'user1@fake.com')
# database.add_user(user1)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/initdb")
async def root():
    # Create various users
    user1 = User('user1', 'password', 'user1@fake.com')
    user2 = User('user2', 'password2', 'user2@fake.com')
    user3 = User('user3', 'password3', 'user3@fake.com')

    post1 = Post(category='computing', text='computing is fun', user_id=user1.id)
    post2 = Post(category='movie', text='Matrix is fun', user_id=user2.id)
    post3 = Post(category='science', text='Science is fun', user_id=user2.id)
    post4 = Post(category='movie', text='Movie is even more fun', user_id=user3.id)

    database.add_user(user1)
    database.add_user(user2)
    database.add_user(user3)
    database.add_user(post1)
    database.add_user(post2)
    database.add_user(post3)
    database.add_user(post4)
    return {"db init": "OK"}


@app.get("/reset_all")
def reset_all_tables():
    database.recreate_all_tables()


@app.get("/users")
def get_all_users():
    users = database.get_all_users()
    users_list = [u.as_dict() for u in users]
    return users_list

@app.get("/posts")
def get_all_posts():
    posts = database.get_all_posts()
    posts_list = [p.as_dict() for p in posts]
    return posts_list


@app.get("/posts/{user_id}")
async def get_posts_from_user_id(user_id: int):
    """
    Retrieve a user based on their id
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """
    results = database.get_posts_and_users_from_userid(user_id)
    return results

@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int):
    """
    Retrieve a user based on their id
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """
    user = database.get_user_by_id(user_id)
    return user.as_dict()


@app.post("/user/")
async def add(username: str, password: str, email: str):
    """
    Retrieve a user based on their id
    :param email:
    :param password:
    :param username:
    :return: a dict containing the user info
    """
    user = User(username, password, email)
    database.add_user(user)
    return user.as_dict()


@app.put("/user/{user_id}")
async def add(user_id: int, username: Optional[str] = None,
              password: Optional[str] = None,
              email: Optional[str] = None):
    """
    Retrieve a user based on their id
    :param username:
    :param email:
    :param password:
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """

    user = database.get_user_by_id(user_id)
    user.username = username if username else user.username
    user.password = password if password else user.password
    user.email = email if email else user.email
    database.add_user(user)
    return user.as_dict()


@app.delete("/user/{user_id}")
async def add(user_id: int):
    """
    Retrieve a user based on their id
    :param user_id: the id of the user to retrieve
    :return: a dict containing the user info
    """
    database.delete_user_by_id(user_id)
    return {'deleted': f'user_id {user_id}'}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# class User(BaseModel):
#     id: int
#     username: str
#     password: str
#     email: str
#
# class Post(BaseModel):
#     id: int
#     category: str
#     text: str
#     user_id: int
#
# @app.post("/users/")
# async def create_user(user: User):
#     return user
