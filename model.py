from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)


engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")

Base.metadata.create_all(engine)
