# Tic Tac Toe Game
# This program allows two players to play the classic Tic Tac Toe game on a graphical user interface (GUI).
import random
from tkinter import *

def next_turn(row, column):
    """
    Handles the logic for the next turn in the Tic Tac Toe game.
    """
    global player

    if buttons[row][column]['text'] == '' and check() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check() is False:
                player = players[1]
                l.config(text=(players[1]+' turn'))
            elif check() is True:
                l.config(text=players[0]+' wins')
            elif check() == 'Tie':
                l.config(text='Tie')
        else:
            buttons[row][column]['text'] = player
            if check() is False:
                player = players[0]
                l.config(text=(players[0]+' turn'))
            elif check() is True:
                l.config(text=players[1]+' wins')
            elif check() == 'Tie':
                l.config(text='Tie')

def check():
    """
    Checks if there is a winner or a tie in the Tic Tac Toe game.
    """
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg='light green')
            buttons[row][1].config(bg='light green')
            buttons[row][2].config(bg='light green')
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg='light green')
            buttons[1][column].config(bg='light green')
            buttons[2][column].config(bg='light green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='light green')
        buttons[1][1].config(bg='light green')
        buttons[2][2].config(bg='light green')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='light green')
        buttons[1][1].config(bg='light green')
        buttons[2][0].config(bg='light green')
        return True
    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='yellow')
        return 'Tie'
    else:
        return False

def empty_space():
    """
    Checks if there are any empty spaces left on the Tic Tac Toe board.
    """
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    """
    Starts a new game of Tic Tac Toe.
    """
    global player
    player = random.choice(players)
    l.config(text=player + ' turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg='white')

# Set up the GUI window
w = Tk()
w.title('Tic Tac Toe')
w.geometry('500x500')

players = ['x', 'o']
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

l = Label(text=player+' turn', font=('consolas', 20))
l.pack(side=TOP)

reset_button = Button(text='Restart', font=('consolas', 30), command=new_game)
reset_button.pack(side=TOP)

f = Frame(w)
f.pack()

# Create the Tic Tac Toe buttons grid
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(f, text='', font=('consolas', 15), bg='white', width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

w.mainloop()
