import os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ToDo(Base):
    """docstring for Todo"""
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    created_ts = Column(DateTime)


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    todos_id = Column(Integer)  # creatng a relationship between the two tables
    items = Column(String(255))


if __name__ == '__main__':
    engine = create_engine('sqlite:///./database.db')
    Base.metadata.create_all(bind=engine)
