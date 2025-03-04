# database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:University456456@localhost/buisinessproject"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    news_id = Column(Integer, ForeignKey("news.id"))
    image_url = Column(String)

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    author_id = Column(Integer, ForeignKey("reporter.id"))
    editor_id = Column(Integer, ForeignKey("reporter.id"))
    datetime = Column(DateTime)
    title = Column(String)
    body = Column(String)
    link = Column(String)

class Publisher(Base):
    __tablename__ = "publisher"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    head_office_address = Column(String)
    website = Column(String)
    facebook = Column(String)
    twitter = Column(String)
    linkedin = Column(String)
    instagram = Column(String)

class Reporter(Base):
    __tablename__ = "reporter"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    news_id = Column(Integer, ForeignKey("news.id"))
    summary_text = Column(String)

Base.metadata.create_all(bind=engine)