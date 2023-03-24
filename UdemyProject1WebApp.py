import streamlit as smlt
import os
import Functions

#sample/initial todos
# sample_todos=["wake up","drink water","brush teeth","wash face","dress into day clothes"]

# smlt.text(os.path.exists("todos.txt"))

todo_list=Functions.get_todos()

def add_todo():
    new_todo= smlt.session_state["add_item"]+"\n"
    todo_list.append(new_todo)
    Functions.write_todos(todo_list)

 
#Section for defining and setting Web App elements
smlt.title("Simple To-Do App")
smlt.subheader("by IsmailJogiat Inc")
smlt.text("A simple and easy to-do app that allows adding, editing and completing to-do items")
smlt.text("Select the checkbox next to the to do item to mark it completed")

#creates check boxes for every to-do item. 
for index,todo in enumerate(todo_list):
    #when checkbox is checked by user it returns True
    check_status= smlt.checkbox(todo, key=todo)
    
    #if an item is checked we want to remove it from the text file and the web page
    if check_status:
        todo_list.pop(index)
        Functions.write_todos(todo_list)
        del smlt.session_state[todo]
        smlt.experimental_rerun()


smlt.text_input(label="Enter an item to add to the list: ", placeholder="add item...",on_change=add_todo,key="add_item")





    

