import os
import click
from colorama import Back, Fore
from pyfiglet import Figlet


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base, ToDo, Items

engine = create_engine('sqlite:///./database.db')
Base.metadata.bind = engine

#associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_todo(name):
    """  
    Add a new TODO item 

    """
    todo = ToDo(name = name)
    session.add(todo)
    session.commit()
    print (Back.GREEN + "{} added successfully".format(todo))


def open_todo(name):
    """opens the todo """
    todo = session.query(ToDo).filter(ToDo.name==name).first()
    print(Fore.RED + "Opening... " + todo.name)
    return todo


def add_item(todo, item):
    """Add a new item to the todo list"""
  
    new_item = Items(todo_id=todo.id,name=item)
    session.add(new_item)
    session.commit()

def exit_todo():
    pass



# if __name__ == '__main__':
#     cli()
