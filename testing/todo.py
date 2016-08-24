import os

from firebase import firebase
import click
import colorama
from pyfiglet import Figlet


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import select
from models import Base, ToDo, Items

engine = create_engine('sqlite:///./database.db')
Base.metadata.create_all(bind=engine)

#associate with the custom Session class
DBSession = sessionmaker(bind=engine)
session = DBSession()

f = Figlet(font='slant')

def display_todo_titlebar():
    '''  displays a title bar.'''
    # os.system('clear')
    print("\t**************************************************")
    print f.renderText('Jipange App')
    print("\t***************************************************")


def create_todo(name):
    """  
    Add a new TODO item 
    """
    todo = ToDo('name', 'id', )
    session.add(todo)
    session.commit()
    print 'todo successfully created'





def open_todo(name):
    """opens the todo """

   

    s = select([ToDo])
    result = s.execute()
    for row in result:
        if row[1] == name:
            # Find all Items 
            q = session.query(Item).filter(Item.todo_id==row[0].all())
            for f in q:
                print 'f.items'



def add_item(self):
	"""Add a new item to the todo list"""
    item = ToDo(name='new item')
    session.add(new_item)
    session.commit()


   
print open_todo('name')	

# if __name__ == '__main__':
    
 