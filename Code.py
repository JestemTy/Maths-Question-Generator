from tkinter import *
from tkinter import ttk
import random

# Run commands for each button
def addition():
    a = int(range_num.get())
    b = int(Numof_q.get())
    output.delete("1.0", END)  # Clear previous questions
    for Question_num in range(b):
        Question = f"{random.randrange(a)} + {random.randrange(a)} ="
        #ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)
        output.insert(END, Question + "\n")

def subtraction():
    a = int(range_num.get())
    b = int(Numof_q.get())
    output.delete("1.0", END)  # Clear previous questions
    for Question_num in range(b):
        Question = f"{random.randrange(a)} - {random.randrange(a)} ="
        #ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)
        output.insert(END, Question + "\n")

def divide():
    a = int(range_num.get())
    b = int(Numof_q.get())
    output.delete("1.0", END)  # Clear previous questions
    for Question_num in range(b):
        Question = f"{random.randrange(a)} ÷ {random.randrange(a)} ="
        #ttk.Label(frm, text=Question).grid(columnspan=4, row=8 + Question_num)
        output.insert(END, Question + "\n")

def multiply():
    a = int(range_num.get())
    b = int(Numof_q.get())
    output.delete("1.0", END)  # Clear previous questions
    for Question_num in range(b):
        Question = f"{random.randrange(a)} x {random.randrange(a)} ="
        #ttk.Label(frm,Question).grid(columnspan=4, row=8 + Question_num)
        output.insert(END, Question + "\n")

# Obsolete
# def mathgen():
#    a = int(range_num.get())
#    b = int(Numof_q.get())
#    for Question_num in range(b):
#        Question = f"{random.randrange(a)} + {random.randrange(a)} ="
#        ttk.Label(frm, text=Question, style="TLabel").grid(columnspan=4, row=8 + Question_num)

# Create GUI Window
root = Tk()
root.title("Math Gen")
frm = ttk.Frame(root, padding=10)
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
#ttk.Button(frm, text="Run", command=mathgen).grid(column=2, row=6) ----obsolete

# Frame to hold the questions and scrollbar
output_frame = ttk.Frame(frm)
output_frame.grid(
    column=0, row=6, columnspan=5,
    sticky="nsew", pady=10
)

# Scrollable, copyable question box
output = Text(
    output_frame,
    width=40,
    height=15,
    wrap="word"
)
output.grid(row=0, column=0, sticky="nsew")

# Vertical scrollbar
scrollbar = ttk.Scrollbar(
    output_frame,
    orient="vertical",
    command=output.yview
)
scrollbar.grid(row=0, column=1, sticky="ns")

output.configure(yscrollcommand=scrollbar.set)

# Allow the text box to expand
output_frame.columnconfigure(0, weight=1)
output_frame.rowconfigure(0, weight=1)

root.mainloop()