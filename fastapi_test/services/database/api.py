from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi_test.services.database.tables.models import Base, User, Post
from fastapi_test.services.database.schemas import UserSchema


class DBApi():
    def __init__(self, db_url):
        self.base = Base
        self.engine = create_engine(db_url)
        self.session = self.create_session(self.engine)

    def create_all_tables(self):
        self.base.metadata.create_all(self.engine)

    def get_all_users(self) -> [User,...]:
        users = self.session.query(User).all()
        return users

    def get_all_posts(self) -> [Post,...]:
        posts = self.session.query(Post).all()
        return posts

    def recreate_all_tables(self):
        self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)

    def create_session(self, engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    def get_user_by_id(self, uid: int) -> User | None:
        print(uid)
        user = self.session.get(User, uid)
        return user

    def delete_user_by_id(self, uid):
        user = self.session.get(User,uid)
        self.session.delete(user)
        self.session.commit()

    def get_posts_and_users_from_userid(self, uid: int):
        results = self.session.query(Post, User).filter(Post.user_id==User.id).filter(User.id==uid).all()
        return results

    def get_posts_and_users_from_category(self, category: str):
        results = self.session.query(Post, User).filter(User.id==Post.user_id).filter(Post.category==category).all()
        return results

    def add_user(self, user_schema: UserSchema):
        self.session.add(user_schema)
        self.session.commit()

    # def add_post(self, post: Post):
    #     self.session.add(post)
    #     self.session.commit()
    #
    # def get_all_users(self):
    #     all_users = self.session.query(User).all()
    #     return all_users
    #
    # def get_user_by_username(self, username: str):
    #     all_users = self.session.query(User).filter(User.username==username).all()
    #     return all_users
    #
    #
    #
    # def get_all_posts(self):
    #     all_posts = self.session.query(Post).all()
    #     return all_posts
    #
    # def get_all_by_category(self, category: str):
    #     all_posts = self.session.query(Post).filter(Post.category == category).all()
    #     return all_posts
    #

