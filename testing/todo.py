import os
import sqlite3
from firebase import firebase
import click
import colorama

# db_filename = 'todo.db'
db_is_new = not os.path.exists('todo.db')

# checks for eixisting db if it doesnt exist,new db created
conn = sqlite3.connect('todo.db')
c = conn.cursor()





conn.close()
