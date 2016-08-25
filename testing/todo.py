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

@click.group()
def cli():
    pass





def display_todo_titlebar():
    '''  displays a title bar.'''
    # os.system('clear')
    print("\t********************************************************")
    print f.renderText('Jipange App')
    print("\t********************************************************")


def show_menu():
    print "1. create todo"
    print "2. Add Items to your Todo"
    print "3. list all items"
    print "q"

@cli.command()
@click.option('--create')
@click.option('--add')
@click.option('--open')
@click.option('--lists')
@click.option('--listall', is_flag=True)
def main(create, add, open, lists, listall):
    display_todo_titlebar()
    show_menu()

    if create is not None:
        create_todo(create)
    if add is not None:
        add_item(add[0])
    if open is not None:
        open_todo(open)
    # if lists is not None:
    #     list_todo(lists)
    # if listall is not None:
    #     list_all_todos(listall)



def create_todo(name):
    """  
    Add a new TODO item 

    """
    todo1 = name


    todo = ToDo(name = todo1)
    session.add(todo)
    session.commit()

    print 'todo successfully created'

        # open_todo(name)





def open_todo(name):
    """opens the todo """

    s = select([ToDo])
    import ipdb; ipdb.set_trace();
    result = engine.execute("select name from todos")
    for row in result:
        if row[''] == name:
            # Find all Items 
            q = session.query(Items).filter(Items.todo_id==row[0]).all()
            for f in q:
                return f.items



def add_item(name, item):
    """Add a new item to the todo list"""
    s = session([ToDo])
    result = s.execute()
    for row in result:
        if row[1] != name:
            return None
        else:
            new_item = Items(todo_id=r[0], items=item, completed= datatime)
            session.add(new_item)
            session.commit()





def exit_todo():
    pass



if __name__ == '__main__':
    cli()
