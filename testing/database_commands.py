from models import ToDo, Items
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///./database.db')

Base = declarative_base
# Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_todo(name):
	add_todo = ToDo(name=name)
	session.commit(add_todo)
	return "ToDo: " + name + " created!"

def add_item(item, todo_name):
	add_item = Items(todo_name=todo_name, items=item)
	# print(add_item)
	session.commit(add_item)
	return "Item: " + str(item) + " Saved To: " + str(todo_name)

def main():
	print(add_item('The Item','learn python'))

if __name__ == '__main__':
	main()


"""
todos
{
	todo_id
	name
	created_ts
}

items
{
	item_id
	todo_id
	description
}
"""