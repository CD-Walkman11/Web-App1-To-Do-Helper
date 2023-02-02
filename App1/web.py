import streamlit as st
import functions as fnc

todos = fnc.get_todos()

st.title("To-Do List Helper")
st.subheader("A Productivity List Creator")
st.write("What would you like to do today?")

for todo in todos:
    st.checkbox(todo)


st.text_input(label='', placeholder="Enter a To-Do...")
