import tkinter as tk
from tkinter import messagebox as mbox
from random import randint, choice

buttons = []
board = []
def place_buttons():
    """Creates, sets up and places the buttons."""
    global buttons, board
    buttons=[]
    for y in range(3):
        for x in range(3):
            button = tk.Button(window, height=1, width=5, font=("Arial", "25", "bold"))
            button.grid(row=y, column=x)
            button.bind("<Button-1>", clicked)
            # button.bind("<Button-3>", clicked2) # right click to play "x" for testing
            buttons.append(button)

    board = [[None,None,None],
            [None,"x",None],
            [None,None,None]]

    midButton = buttons[4]
    midButton.config(text="X", disabledforeground="red", state=tk.DISABLED)
    midButton.unbind("<Button-1>")
    midButton.unbind("<Button-3>")

def won(winner="draw"):
    """Unbinds all buttons and displays winner message, or draw message. give option to quit, play again or view the board"""
    for b in buttons:
        b.unbind("<Button-1>")
        b.unbind("<Button-3>")
    
    if winner == "draw":
        msg = "draw, nobody wins\ntry again?"
    else:
        msg = f"Congratulations {winner}, well done\nplay again?"

    rertyOrQuit = mbox.askyesnocancel(f"{winner}!",msg)
    if rertyOrQuit: 
        place_buttons()
    elif not None:
        window.destroy()



def checkForWinner(gameList):
    """Checks if anyone has won the game"""    
    #rows and columns
    for i in range(len(gameList)):
        row = set()
        col = set()

        for x in range(len(gameList[i])):
            row.add(gameList[i][x])
            col.add(gameList[x][i])

        if None not in row and len(row) == 1:
            won(list(row)[0])
            return list(row)[0]

        if None not in col and len(col) == 1:
            won(list(col)[0])
            return list(col)[0]

    #diagonals  
    mid = len(gameList)//2
    if gameList[mid][mid] != None:
        diagL = set()
        for pos in range(len(gameList)):
            diagL.add(gameList[pos][pos])

        if None not in diagL and len(diagL) == 1:
            won(list(diagL)[0])
            return list(diagL)[0]
        
        diagR = set()
        for pos in range(len(gameList)):
            diagR.add(gameList[pos][-(pos+1)])

        if None not in diagR and len(diagR) == 1:
            won(list(diagR)[0])
            return list(diagR)[0]


    # draw
    for position in gameList:
        if None in position:
            return False
    won()
    return "draw"
    
def possible_moves():
    """creates dict of possible moves with tuple of button position from 2d 'board' array as values"""
    avaliableMoves = {}
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == None:
                if x in avaliableMoves:
                    avaliableMoves[x][y]=(x,y)
                else:
                    avaliableMoves[x]={}
                    avaliableMoves[x][y]=(x,y)
    return avaliableMoves


def comp_play():
    """Plays computer players move picked at random from dict of available positions."""
    avaliableForComp = possible_moves()

    i = choice(list(avaliableForComp.keys()))
    (x,y) = choice(list(avaliableForComp[i].values()))
    
    pos = x*3+y # convert index for 2D array into index for 1D array 'buttons'
    
    pickedButton = buttons[pos]
    pickedButton.config(text="X", disabledforeground="red", state=tk.DISABLED)
    pickedButton.unbind("<Button-1>")
    pickedButton.unbind("<Button-3>")

    board[x][y] = "x"
    checkForWinner(board)
    

def clicked(e):
    """Set button clicked by player to green "O" and update the board.
    Check if that was a winning move, if not then run comp_play().
    """
    e.widget.config(text="O", disabledforeground="green", state=tk.DISABLED)
    e.widget.unbind("<Button-1>")
    e.widget.unbind("<Button-3>")
    
    pos = buttons.index(e.widget)
    x=pos//3
    y=pos%3
    
    board[x][y] = "o"
    
    if not checkForWinner(board):
        comp_play()

def clicked2(e):
    """Set button clicked by player to red "X" and update the board.
    Check if that was a winning move, if not then run comp_play().
    
    Used for testing.
    """
    e.widget.config(text="X", disabledforeground="red", state=tk.DISABLED)
    e.widget.unbind("<Button-3>")
    e.widget.unbind("<Button-1>")
    
    pos = buttons.index(e.widget)
    x=pos//3
    y=pos%3

    board[x][y] = "x"

    if not checkForWinner(board):
        comp_play()
    

#gui setup and layout
window = tk.Tk()
window.title("Tic Tac Toe")

place_buttons()

retry = tk.Button(window, text="retry", command=place_buttons)
retry.grid(row=4,column=1)

# cmp_ply_btn = tk.Button(window,text="cmp ply",command=comp_play) #used to force comp_play for testing
# cmp_ply_btn.grid(row=4,column=2)
window.mainloop()
