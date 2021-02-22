"""
pocket calculator 
by Bailey Jordan-Hunter
https://github.com/Bjordanhunter/PCPP-projects/blob/main/pocket_calculator/pocket_calculator.py

part of edube.org PCPP GUI course work (https://edube.org/learn/pcpp1-4-gui-programming/project-pocket-calculator)
"""
import tkinter as tk


#helper/layout functions
def place_numpad_in_order(numpadButtons):
    """places the number pad buttons in order (left to right,top to bottom): 789,456,123"""
    numpadButtons.insert(0,numpadButtons.pop(-1)) # move "0" button to front of list to aid loop indexing
    
    for y in range(0,9,3):
        rowBtns = numpadButtons[y+3:y:-1] 
        for x in range(3):
            rowBtns[x].grid(row=y//3+1, column=x)
    
    numpadButtons[0].grid(row=4, column=1)

def make_and_place_numpad_buttons():
    """makes number pad buttons"""
    global buttonFont
    numpadButtons = []
    
    for num in range(9,-1,-1):
        btn = tk.Button(window, text=num, font=buttonFont, width=buttonWidth, takefocus=False)
        btn.bind(defualtMouseKey, append_num_to_display)
        numpadButtons.append(btn)
	
    place_numpad_in_order(numpadButtons)
			
def make_and_place_operation_buttons():
    """makes and places the +,-,*,/,= operator buttons"""
    ops = ["+","-","*","/"]
    for opAndRow in range(len(ops)):
        btn = tk.Button(window, text=ops[opAndRow], font=buttonFont, width=buttonWidth, takefocus=False)
        btn.bind(defualtMouseKey, set_operation)
        btn.grid(row=opAndRow+1, column=4)
    
    btn = tk.Button(window, text="=", font=buttonFont, width=buttonWidth, takefocus=False)
    btn.bind(defualtMouseKey, perform_operation)
    btn.grid(row=4,column=3)

def trim_after_decimal(x):
    """returns int or float trimed down with string formating to keep as many significant digits after decimal as posible, 
    alwoys at least 1 significant digit and always 10
    e.g. 1/3=0.33333333, 10000000/3=33333333.3, -1/3=-3.3333333
    """
    if x == errorMessage: return x
    x = float(x)
    if x == int(x):
        return int(x)  
    else:

        x = f"{x:.9g}"
        x = x if len(x) <= 10 else f"{float(x):.8g}" # edge case of 0.x nums (weird)
        x = x if len(x) <= 10 else f"{float(x):.7g}" # accounting for minus sign
        return float(x)

def run_bound_function(e):
    """gets and runs the function bound to a given event widget and passes it the event, simulating being clicked.
    needed so as to avoid having to click twice after the calculator clears it's self after error or continous operations.
    gets function name from inside a tcl command string 
    """
    funcName = e.widget.bind(defualtMouseKey)
    if not funcName: return

    funcName = funcName[19:funcName.index(" ",19)] 
    globals()[funcName](e)

def clear_display(e=None):
    """clears only the display when anything is clicked after continuous operations"""
    displayOutput.set(0)
    window.unbind_all(defualtMouseKey)
    run_bound_function(e)


#button functions
def clear_display_and_memory(e=None):
    """resets display and numOneMemory back to 0 and operation to empty string."""
    global numOneMemory, operation
    displayOutput.set(0)
    operation = ""
    numOneMemory = 0
    window.unbind_all(defualtMouseKey)
    window.focus_set()
    if e.widget["text"] != "C":
        run_bound_function(e)

def backspace(e=None):
    """removes the last charecter of the display"""
    currDisplayStr = displayOutput.get()
    if len(currDisplayStr) == 1 or ("-" in currDisplayStr and len(currDisplayStr) == 2): 
        displayOutput.set(0)
    else:
        displayOutput.set(currDisplayStr[:-1])
    e.widget.focus_set()

def append_num_to_display(e):
    """add chosen number to the end of the display"""
    global maxDisplayLength
    currDisplayStr = displayOutput.get()
    if len(currDisplayStr) >= maxDisplayLength: return
    
    num = e.widget["text"]
    if currDisplayStr == "0": 
        displayOutput.set(num)
    else:
        displayOutput.set(currDisplayStr+str(num))

def append_decimal_to_display(e=None):
    """adds a decimal point to number on display"""
    currDisplayStr = displayOutput.get()
    if len(currDisplayStr) >= maxDisplayLength or "." in currDisplayStr : return

    displayOutput.set(currDisplayStr+".")

def invert_display_num(e=None):
    """changes the displayed number to a negative or a positive"""
    currDisplayStr = displayOutput.get()
    if len(currDisplayStr) >= maxDisplayLength and "-" not in currDisplayStr: return

    displayOutput.set(trim_after_decimal(currDisplayStr)*-1)

def set_operation(e=None):
    """set the operation to perform and saves current number to memory"""
    global numOneMemory, operation
    
    if operation: 
        perform_operation()
    else:
        numOneMemory = float(displayOutput.get())
        displayOutput.set(0)
    operation = e.widget["text"]
    e.widget.focus_set()

def perform_operation(e=None):
    """performs operation saved in 'operation' on numOneMemory and current number on display.
    Trims any insignificant digits (trailing zeros) after decimal.
    Displays errorMessage if resulting number is to long or creates division by zero error.

    Could use 'numexpr' to elauate from strings (numexpr.evaluate(numOneMemory+operation+numTwo)) but it would 
    require large(ish) packages numexpr and numpy, and is not really necessary given application scope.
    """
    global numOneMemory, operation
    currDisplayStr = displayOutput.get()
    if not operation or errorMessage in (numOneMemory, currDisplayStr) : return

    numTwo = float(currDisplayStr)
    if operation == "+":
        result = numOneMemory+numTwo
    elif operation == "-":
        result = numOneMemory-numTwo
    elif operation == "*":
        result = numOneMemory*numTwo
    elif operation == "/":
        try:
            result = numOneMemory/numTwo
        except ZeroDivisionError:
            result = errorMessage
    
    result = trim_after_decimal(result)
    if len(str(result)) > maxDisplayLength:
        result = errorMessage
    elif not e:
        numOneMemory = result
    elif e:
        operation = ""
        e.widget.focus_set()
    
    displayOutput.set(result)
    if result == errorMessage:
        window.bind_all(defualtMouseKey, clear_display_and_memory, "+")
    else:
        window.bind_all(defualtMouseKey, clear_display, "+")

#options
errorMessage = "ERROR!"
maxDisplayLength = 10
buttonFont = ("Courier New", 15, "normal")
buttonWidth = 2
defualtMouseKey = "<1>"

numOneMemory = 0
operation = ""

#GUI setup 
window = tk.Tk()
window.title("Pocket Claculator")
window.resizable(width=False, height=False)
window.tk_focusFollowsMouse()

displayOutput = tk.StringVar()
displayOutput.set(0)#
display = tk.Label(window, textvariable=displayOutput, font=("Courier New", 20, "bold"), width=maxDisplayLength, anchor="e")

clearBtn = tk.Button(window, text="C", font=buttonFont, width=buttonWidth, takefocus=False)
clearBtn.bind(defualtMouseKey, clear_display_and_memory)

bkspBtn = tk.Button(window, text="¬", font=buttonFont, width=buttonWidth, takefocus=False)
bkspBtn.bind(defualtMouseKey, backspace)

decimalBtn = tk.Button(window, text=".", font=buttonFont, width=buttonWidth, takefocus=False)
decimalBtn.bind(defualtMouseKey, append_decimal_to_display)

invertBtn = tk.Button(window, text="+/-", font=buttonFont, width=buttonWidth, takefocus=False)
invertBtn.bind(defualtMouseKey, invert_display_num)

blankBtn = tk.Button(window, font=buttonFont, width=buttonWidth, state="disabled", takefocus=False) #exsists to fill a gap

#GUI layout
display.grid(row=0, columnspan=5)

make_and_place_numpad_buttons()
make_and_place_operation_buttons()

decimalBtn.grid(row=4,column=2)
bkspBtn.grid(row=4, column=0)

invertBtn.grid(row=1, column=3)
clearBtn.grid(row=2, column=3)
blankBtn.grid(row=3, column=3)

window.mainloop()