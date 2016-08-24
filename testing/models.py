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


if __name__ == '__main__':
    engine = create_engine('sqlite:///./database.db')
    Base.metadata.create_all(bind=engine)


# COMMANDS

# @click.group()  # group decorator can be given multiple commands
# def cli():


# @click.command()
# def initdb():
#     click.echo('Initialized database')

  # decorator coverts function to a command
# def hello():
#     click.echo('Hello world!')

# cli.add_command(initdb)
