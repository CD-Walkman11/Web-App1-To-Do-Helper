import functions as fnc
import PySimpleGUI as sg

label = sg.Text("Enter a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key='todo')
add_button = sg.Button('Add')

list_box = sg.Listbox(values=fnc.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

layout = [[label, input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do Helper',
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case 'Add':
            todos = fnc.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fnc.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = fnc.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fnc.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = fnc.get_todos()
            todos.remove(todo_to_complete)
            fnc.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
