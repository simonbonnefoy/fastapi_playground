from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

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

engine = create_engine(f"sqlite:///test_sqlite.db")

# Create all tables in the DB
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create various users
user1 = User('user1', 'password', 'user1@fake.com')
user2 = User('user2', 'password2', 'user2@fake.com')
user3 = User('user3', 'password2', 'user3@fake.com')

# Add users to the databaset
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

# Add a post to users
post1 = Post(category='computing', text='computing is fun', user_id = user1.id)
post2 = Post(category='movie', text='Matrix is fun', user_id = user2.id)
post3 = Post(category='science', text='Science is fun', user_id = user2.id)
post4 = Post(category='movie', text='Movie is even more fun', user_id = user3.id)

session.add(post1)
session.add(post2)
session.add(post3)
session.add(post4)

session.commit()

#################
# Read database
#################

# Retrieve all entries
results_all = session.query(User).all()

# Retrieve entries based on filter
user1 = session.query(User).filter(User.email=="user1@fake.com").all()
#results = session.query(User, Post).filter(Post.user_id==User.id).filter(User.id == 1).filter(Post.category=='movie').all()

# Retrieve entries from User and Post based on filters
results = session.query(Post, User).filter(Post.user_id==User.id).filter(User.id == 2).filter(Post.category=='movie').all()
for (post, user) in results:
    print(post.id)
    print(user.id)
