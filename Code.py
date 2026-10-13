from tkinter import *
from tkinter import ttk
import random

# Colours
bg = "#DE1938"
fg = "#9cde51"
tx = "#5a51de"

#Style
style = ttk.Style()
style.configure("SFrame", background=bg)
style.configure("TButton", background=fg, foreground=tx, font=('arial', 12, 'bold'))
style.configure("TLabel", background=fg, foreground=tx, font=('arial', 12, 'bold'))

# Run commands for each button
def addition():
    a = int(range_num.get())
    b = int(Numof_q.get())
    for Question_num in range(b):
        Question = f"{random.randrange(a)} + {random.randrange(a)} ="
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
        ttk.Label(frm, text=Question, style="TLabel").grid(columnspan=4, row=8 + Question_num)

 # Create GUI Window
root = Tk()
root.title("Math Gen")
frm = ttk.Frame(root, padding=10, style="SFrame")
frm.grid()

ttk.Label(frm, text="Generate a list of math questions", style="TLabel").grid(columnspan=4, row=0)

ttk.Label(frm, text="In the range of (10, 100)", style="TLabel").grid(column=0, row=2)
range_num = ttk.Entry(frm, width=10)
range_num.grid(column=1, row=2)

ttk.Label(frm, text="Number of questions (1, 5, 10)").grid(column=0, row=3)
Numof_q = ttk.Entry(frm, width=10)
Numof_q.grid(column=1, row=3)

ttk.Label(frm, text="Type of Questions (+,-,/,*)", style="TLabel").grid(column=0, row=4)
ttk.Button(frm, text="Addition", command=addition, style="TButton").grid(column=1, row=4)
ttk.Button(frm, text="Subtraction", command=subtraction, style="TButton").grid(column=2, row=4)
ttk.Button(frm, text="Division", command=divide, style="TButton").grid(column=3, row=4)
ttk.Button(frm, text="Multiplication", command=multiply, style="TButton").grid(column=4, row=4)
#ttk.Button(frm, text="Run", command=mathgen).grid(column=2, row=6)

root.mainloop()