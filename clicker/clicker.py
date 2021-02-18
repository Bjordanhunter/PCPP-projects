import tkinter as tk
from random import randint

def get_num():
    """Gets a random number that is not already in 'nums'."""
    global nums
    n = randint(1,999)
    if n in nums:
        return get_num()
    else:
        nums.append(n)
        return n

def make_buttons(numOfButtons):
    """Makes buttons with unique random numbers and adds them to dictionary with corresponding number as value. """
    for _ in range(numOfButtons):
        n = get_num()
        
        button = tk.Button(window, text=n, width=10)
        button.bind("<Button-1>",click)

        buttons[button] = n

def place_buttons():
    """places all the button from dict:'buttons' in a 5 wide grid"""
    global buttons
    x,y=0,0
    for b in buttons.keys():
        b.grid(column=x,row=y)
        x += 1
        if x >= 5:
            y += 1
            x = 0

def click(e):
    """Checks if button clicked is next in sequence, if so disables it and grays it out. If sequence is finished stops timer."""
    global buttons
    global nums
    global timer
    num = buttons[e.widget]
    if nums.index(num) == 0:
        e.widget.config(state=tk.DISABLED, bg="light gray") #sets background to gray as well as it was hard to tell without
        e.widget.unbind("<Button-1>")
        nums.remove(num)
        left.set(str(25-len(nums))+"/25")
    if not nums:
        window.after_cancel(timer)

def inc_time():
    """Increments timer and set to be call again in 1 second."""
    global timer
    time.set(time.get()+1)
    timer = window.after(1000,inc_time)

def start_timer(_):
    """Starts timer on first click"""
    time.set(0)
    window.after(1000,inc_time)
    window.unbind("<Button-1>")

#gui setup and layout
window = tk.Tk()

buttons = {}
nums=[]
time = tk.IntVar()
left = tk.StringVar()

make_buttons(25)
place_buttons()
nums.sort()

timerMsg = tk.Message(window, textvariable=time)
timerMsg.grid(row=6,column=2)
window.bind("<Button-1>", start_timer) # only used one to start timer on first click

left.set(str(25-len(nums))+"/25")
progress = tk.Message(window, textvariable=left, width=100)
progress.grid(column=0, row=6, columnspan=2)

quit = tk.Button(window, text="Quit", borderwidth=0, command=window.destroy)
quit.grid(column=3, row=6, columnspan=2)

window.mainloop()
