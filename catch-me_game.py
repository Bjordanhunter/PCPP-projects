import tkinter as tk
from tkinter import messagebox as mbox
from random import randint

def randint_not_x(randMin,randMax,x,w_h):
    """Creates a random number within given range (randMin, randMax) 
    where 'x' does not fall in range of n and n+w_h (width or height of button).
    
    limited to 100 attempts to avoid hanging.
    """
    for _ in range(100):
        n = randint(randMin,randMax)
        if x not in range(n,n+w_h):
            return n
    raise Exception("not enough space")
    
def move_button(event=None):
    """Moves button to random position within play area, other then current mouse position."""
    maxX = window.winfo_width()-button.winfo_width()
    maxY = window.winfo_height()-button.winfo_height()
    
    cursorX = button.winfo_x()+event.x
    cursorY = button.winfo_y()+event.y

    newX = randint_not_x(0, maxX, cursorX, button.winfo_width())
    newY = randint_not_x(0, maxY, cursorY, button.winfo_height())
    
    button.place(x=newX,y=newY)

def click_button(event=None):
    """gives win message when button is clicked, although should not be possible"""
    mbox.showinfo(title="You Win!", message="Well done! you win!!\n(although you shouldn't \nhave been able to)")

#gui layout and setup
window = tk.Tk()
window.title("Catch me!")
window.geometry("500x500")

button = tk.Button(window, text="Catch me!")
button.bind("<Enter>",move_button)
button.bind("<Button-1>",click_button)
button.place(x=10,y=10)

window.mainloop()