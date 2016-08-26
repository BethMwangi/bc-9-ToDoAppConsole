import os
import sys
import time
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
import datetime

Base = declarative_base()


class ToDo(Base):
    """create ToDo model"""
    __tablename__ = 'todos'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return "(<ToDo(name='%s', created_ts='%s')>" % (
            self.name, self.created_at)


class Items(Base):
    """create Item model"""
    __tablename__ = 'items'

    id = Column(Integer, autoincrement=True, primary_key=True)
    todo_id = Column(Integer, ForeignKey('todos.id'))
    name = Column(String(255))
    completed = Column(Boolean)
    todo = relationship(ToDo)

    def __repr__(self):
        return "<Item: {0} ToDo: ".format(self.name)

engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)
