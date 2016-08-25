import os
import sys
import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship , backref

Base = declarative_base()


class ToDo(Base):
    """docstring for Todo"""
    __tablename__ = 'todos'

    id = Column(Integer, autoincrement= True, primary_key=True)
    name = Column(String(255), unique=True)
    created_ts = Column(datetime.datetime.utnow)

    def __repr__(self):
        '''passing the constructor'''
        return "(<ToDo(name='%s', created_ts='%s')>" % (
            self.name, self.created_ts)



class Items(Base):

  __tablename__ = 'items'
  item_id = Column(Integer, primary_key=True)
  todos_id = Column(Integer)
  items = Column(String(255))
  completed = Column(Boolean)

  def __repr__(self):
    return '({0}:{1.items})'.format(Items, self)

if __name__ == '__main__':
    engine = create_engine('sqlite:///./database.db')
    Base.metadata.create_all(bind=engine)
