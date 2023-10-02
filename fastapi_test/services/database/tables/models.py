from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    password = Column(String(25), nullable=False, unique=False)
    email = Column(String(25), nullable=False, unique=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return f'{self.username},{self.email}'

    def as_dict(self):
        return {'id':self.id,
                'username': self.username,
                'password': self.password,
                'email': self.email
                }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer(), primary_key=True)
    category = Column(String(25), nullable=False)
    text = Column(String(500), nullable=False)
    user_id = Column(Integer(), ForeignKey('user.id'))

    def __init__(self, category, text, user_id):
        self.category = category
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id} is written by {self.user_id}'

    def as_dict(self):
        return {'id': self.id,
                'category':self.category,
                'text': self.text,
                'user_id': self.user_id
                }
