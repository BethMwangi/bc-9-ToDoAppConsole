import os
import click
from colorama import init, Back, Fore, Style
from pyfiglet import Figlet


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base, ToDo, Items

engine = create_engine('sqlite:///./database.db')
Base.metadata.bind = engine

# associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()


def create_todo(name):
    """  
    Add a new TODO item 

    """
    todo = ToDo(name=name)
    session.add(todo)
    session.commit()
    init(autoreset=True)
    print (Back.GREEN + "{} added successfully".format(todo))


def open_todo(name):
    """opens the todo """
    todo = session.query(ToDo).filter(ToDo.name == name).first()
    print(Fore.RED + "Opening... " + todo.name)
    return todo


def add_item(todo, item):
    """Add a new item to the todo list"""

    new_item = Items(todo_id=todo.id, name=item)
    session.add(new_item)
    session.commit()
    print (Fore.RED + "Successfully added")
    return new_item


def list_all_todos():
    """lists all the todos created"""
    todos = []
    todo_rows = session.query(ToDo).all()
    for todo_row in todo_rows:
        todos.append((todo_row.name, todo_row.created_at))
    # print (Fore.RED +"Listing... " + todos)

    return todos


def list_all_items(name):
    """lists all the todos with items"""
    items = session.query(Items).filter(Items.name).all()
    print(items)
    # count = 1
    # s = select([Items])
    # result = s.execute()
    # if result:
    #     for row in result:
    #         q = session.query(Items).filter(Items.todo_id == row[0]).all()
    #         count += 1
    #         for data in q:
    #             print data.items
                # click.echo(click.style('>>>' + i.items  , fg='white',
                # bold=True)


def exit_todo():
    pass
