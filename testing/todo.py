import os

from firebase import firebase
import click
import colorama


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, ToDo, Items

engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)

#associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()


def display_todo_titlebar():
    ''' Clears the terminal screen, and displays a title bar.'''
    # os.system('clear')
    print("\t**********************************************")
    print click.secho('\t\t Jipange App', fg='green', blink=True)
    print("\t**********************************************")


def new_todo(name):
    """  
    Add a new TODO item 
    """
    todo = ToDo('name', 'id', )
    session.add(todo)
    session.commit()


def add_item(self):
	"""Add a new item to the todo list"""
	

if __name__ == '__main__':
 