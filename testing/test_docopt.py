"""
	Usage:
		Todo create_todo <name> 
		Todo open_todo <name> 
		Todo add_item <name> <item>
		Todo list_all 
		Todo list_todo <name> <item>

	Options:
		-h, --help Show this screen and exit
		--version Show version
"""

from docopt import docopt, DocoptExit
import cmd
import todo
import click
import ui


ui.header_todo()
ui.start()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

todos = []  # List of to dos
todo_items = {}  # Dictionary with todos and its items: "todo_name": [items]


class ToDo(cmd.Cmd):

    # prompt = "todo>>> "
    prompt = click.style(">>>todo", bg='yellow', fg='white', bold='True')

    @docopt_cmd
    def do_create(self, arg):
        """Usage: create <name> """
        name = arg["<name>"]
        todo.create_todo(name)

    @docopt_cmd
    def do_open(self, arg):
        """Usage: open <name> """
        name = arg["<name>"]
        self.todo_name = todo.open_todo(name)

    @docopt_cmd
    def do_add_item(self, arg):
        """Usage: add_item <name> <item>"""
        item = arg["<item>"]
        todo.add_item(self.todo_name, item)

    @docopt_cmd
    def do_list_todo(self, arg):
        """Usage: list_todo <name>"""
        name = arg["<name>"]
        for name in todo.name:
            print (name)

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all"""
        # for todo in todo_items.keys():
        #     print("Items in: " + todo)
        #     items = todo_items[todo]
        #     for item in items:
        #         print(item)
        todos = todo.list_all_todos()
        for the_todo in todos:
        	print("Name: " + the_todo[0])
        	print("Created At: " + str(the_todo[1]))

    # def do_help(self, arg):
    # 	"""Usage:show all commands"""
    # 	ui.help_screen()


if __name__ == '__main__':
    ToDo().cmdloop()
