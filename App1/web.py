import streamlit as st
import functions as fnc

todos = fnc.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    fnc.write_todos(todos)


st.title("To-Do List Helper")
st.subheader("A Productivity List Creator")
st.write("What would you like to do today?")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='', placeholder="Enter a To-Do...",
              on_change=add_todo, key='new_todo')
