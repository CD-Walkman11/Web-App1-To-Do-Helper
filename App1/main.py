# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    # Get and format user input to guarantee if statements
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith('add'):
        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.lower().startswith('show'):
        todos = functions.get_todos()

        # new_todos = [todo.strip('\n') for todo in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}. {item}"
            print(row)

    elif user_action.lower().startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            print(number + 1)

            todos = functions.get_todos()

            todos[number] = input("Enter new Todo: ") + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid Command. Please Try Again.")
            continue

    elif user_action.lower().startswith('complete'):
        try:
            number = int(user_action[9:]) - 1
            print(number + 1)

            todos = functions.get_todos()

            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove}' was removed from the list")
        except IndexError:
            print("There is no Todo with that number.")
            continue

    elif user_action.lower().startswith('exit'):
        break

    else:
        print("Invalid Command")

print("\nHave a Great Day!")
