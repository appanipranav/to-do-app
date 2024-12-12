def get_todos(filepath='todos.txt'):
    """ Read a text file and returns to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath="todos.txt"):
    """ Writing the tod-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)