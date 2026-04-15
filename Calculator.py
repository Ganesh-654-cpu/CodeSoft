from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x450")
root.resizable(False, False)

entry = Entry(root, font=('Arial', 24), bd=8, relief=RIDGE, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

def click(num):
    entry.insert(END, str(num))

def clear():
    entry.delete(0, END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

btn_width = 5
btn_height = 2

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=btn_width, height=btn_height,
               font=('Arial', 14), bg="lightgreen",
               command=equal).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    else:
        Button(root, text=text, width=btn_width, height=btn_height,
               font=('Arial', 14),
               command=lambda t=text: click(t)
               ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

Button(root, text="C", font=('Arial', 14), bg="lightcoral",
       command=clear).grid(row=5, column=0, columnspan=4,
                           sticky="nsew", padx=5, pady=5, ipady=10)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()