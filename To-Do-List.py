from tkinter import *

root = Tk()
root.title("To-Do List")
root.geometry("400x400")
root.config(bg="lightblue")

tasks = []


def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        print("Enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        print("Select a task to delete")


title = Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="lightblue")
title.pack(pady=10)

entry = Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_btn = Button(root, text="Add Task", width=15, command=add_task, bg="blue", fg="white")
add_btn.pack(pady=5)

delete_btn = Button(root, text="Delete Task", width=15, command=delete_task, bg="red", fg="white")
delete_btn.pack(pady=5)

listbox = Listbox(root, font=("Arial", 12), width=30, height=15)
listbox.pack(pady=20)

root.mainloop()