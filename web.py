import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

# GUI visible to the user
st.header("Aaditya's Todo App")
st.text("Keep track of your tasks here!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("Add a todo", placeholder="Add a todo", label_visibility="hidden", on_change=add_todo, key="new_todo")