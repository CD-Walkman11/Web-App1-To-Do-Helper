import functions as fnc
import PySimpleGUI as sg
import time

sg.theme('LightGrey1')

clock = sg.Text('', key='clock')
label1 = sg.Text("Enter a To-Do")
label2 = sg.Text("To-Do List")
input_box = sg.InputText(tooltip="Enter To-Do", key='todo', size=45)
add_button = sg.Button('Add', size=10)
list_box = sg.Listbox(values=fnc.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit', size=9)
complete_button = sg.Button('Complete', size=9)
exit_button = sg.Button('Exit', size=9)

layout = [[clock],
          [label1], [input_box, add_button],
          [label2],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My To-Do Helper',
                   layout=layout,
                   font=('Helvetica', 12))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y | %I:%M:%S"))
    match event:
        case 'Add':
            todos = fnc.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fnc.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = fnc.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fnc.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 12))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = fnc.get_todos()
                todos.remove(todo_to_complete)
                fnc.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 12))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
