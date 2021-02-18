import tkinter  as tk
from tkinter import messagebox as mbox

def checkDigits(num1, num2):
    """Checks nums are valid numbers by attempting to convert to floats. shows error message if not."""
    try:
        return float(num1), float(num2)
    except ValueError:
        mbox.showerror(title="Input Error", message="Both inputs need to numbers")
        
def evaluate():
    """Identifies and evaluates requested operation."""
    num1, num2 = checkDigits(numOne.get(), numTwo.get())
    op = operation.get()
    if op == "+":
        out = num1 + num2
    elif op == "-":
        out = num1 - num2
    elif op == "*":
        out = num1 * num2
    elif op == "/":
        try:
            out = num1 / num2
        except ZeroDivisionError:
            mbox.showerror(title="Zero Division Error", message="You can not divide by zero")
            return
    mbox.showinfo(title="answer",message=str(out))

#gui layout and setup
window = tk.Tk()
window.title("Calculator")

numOne = tk.StringVar()
inputOne = tk.Entry(window, textvariable=numOne)
inputOne.grid(column=1,row=1,rowspan=4)

numTwo = tk.StringVar()
inputTwo = tk.Entry(window, textvariable=numTwo)
inputTwo.grid(column=3,row=1,rowspan=4)

operation = tk.StringVar()
operation.set("+")

add = tk.Radiobutton(window, text="+", variable=operation, value="+")
add.grid(column=2,row=1)

sub = tk.Radiobutton(window, text="-", variable=operation, value="-")
sub.grid(column=2,row=2)

mult = tk.Radiobutton(window, text="*", variable=operation, value="*")
mult.grid(column=2,row=3)

div = tk.Radiobutton(window, text="/", variable=operation, value="/")
div.grid(column=2,row=4)

eval = tk.Button(text="Evaluate", command=evaluate)
eval.grid(column=2,row=5)

window.mainloop()