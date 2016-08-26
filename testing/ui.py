import click
import sys
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from tabulate import tabulate


def header_todo():
	click.secho('$' * 70, fg='yellow')
	click.secho('=' * 70, fg='green')
	cprint(figlet_format('TODO APP', font='banner'),
           'yellow', attrs=['bold'])
	click.secho('=' * 70, fg='green')
	click.secho('$' * 70, fg='yellow')




def start():
	time.sleep(2)
	click.secho(
        """
================LET'S GET STARTED============
GUIDE:
1.CREATE TODO - create <name>
2.OPEN TODO - open <name>
3.ADD ITEM - 	add_item  <item>
4.LIST_ALL - lists todos
5.LIST_TODO -list_all <name> <item>

==============================================
    """, bold=True, fg="yellow")
