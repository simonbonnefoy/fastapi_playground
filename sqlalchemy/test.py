from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import pandas as pd
import sqlite3


Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer(), primary_key=True)
    slug = Column(String(100), nullable=False, unique=True)
    title = Column(String(100), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    content = Column(Text)

engine = create_engine(f"sqlite:///test_sqlite.db")
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add an article 

# article1 = Article(
#     slug="clean-python",
#     title="How to Write Clean Python",
#     content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#     )

Base.metadata.create_all(engine)

# session.add(article1)
# session.commit()


first_article_query = session.query(Article).filter(Article.id == 1)
first_article_df = pd.read_sql(
    sql=first_article_query.statement,
    con=engine
)
first_article_df.to_csv('article.csv')
print(first_article_df['title'])

new_article_df = pd.DataFrame(
    {
        'slug': ['sqlalchemy-pandas'],
        'title': ['SQLAlchemy Pandas Article'],
        'content': ['Bla bla bla'],
    })

# new_article_df.to_sql(
#     name='articles',
#     con=engine,
#     if_exists='append',
#     index=False,
# )

# session.query(Article).filter(
#     Article.slug=='sqlalchemy-pandas'
# ).first().title

## Read csv file and load it into DB
new_df = pd.read_csv("more_articles.csv")

new_df.to_sql(
    name='articles',
    con=engine,
    if_exists='append',
    index=False,
)