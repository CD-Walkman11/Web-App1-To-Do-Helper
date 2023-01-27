def get_todos(file_path='todos.txt'):
    """ Read a text file and return the list
    of to-do items.
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path='todos.txt'):
    """ Write the to-do items list in the text file."""
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)
