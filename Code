from tkinter import *
from tkinter import ttk
import random

def addition():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} + {random.randrange(a)} ="
        #ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)
        ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)

def subtraction():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} - {random.randrange(a)} ="
        ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)

def divide():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} / {random.randrange(a)} ="
        ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)

def multiply():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} x {random.randrange(a)} ="
        ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)

def mathgen():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} + {random.randrange(a)} ="
        ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)
 
root = Tk()
root.title("Math Gen")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Generate a list of math questions").grid(columnspan=4, row=0)

ttk.Label(frm, text="In the range of (10, 100)").grid(column=0, row=2)
range_num = ttk.Entry(frm, width=10)
range_num.grid(column=1, row=2)

ttk.Label(frm, text="Number of questions (1, 5, 10)").grid(column=0, row=3)
Numof_q = ttk.Entry(frm, width=10)
Numof_q.grid(column=1, row=3)

ttk.Label(frm, text="Type of Questions (+,-,/,*)").grid(column=0, row=4)
ttk.Button(frm, text="Addition", command=addition).grid(column=1, row=4)
ttk.Button(frm, text="Subtraction", command=subtraction).grid(column=2, row=4)
ttk.Button(frm, text="Division", command=divide).grid(column=3, row=4)
ttk.Button(frm, text="Multiplication", command=multiply).grid(column=4, row=4)

#ttk.Button(frm, text="Run", command=mathgen).grid(column=2, row=6)

root.mainloop()