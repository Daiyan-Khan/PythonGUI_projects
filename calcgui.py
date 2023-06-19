# File Name: calculator.py

# File Name: calculator.py

# This code implements a basic calculator using the Tkinter library in Python.
# The calculator GUI allows users to perform arithmetic operations such as addition, subtraction,
# multiplication, and division on numbers entered through buttons.
# The result of the calculations is displayed in a label on the GUI.
# The code uses event handlers for button presses, evaluates the entered equation using eval() function,
# and handles errors such as syntax errors and zero division errors.
# It also includes a clear button to reset the calculator and start a new calculation.
# The code demonstrates the usage of Tkinter widgets, event handling, and basic mathematical operations.
# The GUI layout is organized using frames and buttons are placed in a grid-like structure.
# Overall, this code provides a simple implementation of a calculator application in Python.

from tkinter import *

def button_press(num):
    """
    Function to handle button press event for number buttons.
    Updates the equation text and displays it in the equation label.
    """
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    """
    Function to handle button press event for the equals button.
    Evaluates the equation and displays the result in the equation label.
    Handles syntax and zero division errors and displays appropriate messages.
    """
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set('Syntax error')
    except ZeroDivisionError:
        equation_label.set('Arithmetic error')

def clear():
    """
    Function to handle button press event for the clear button.
    Clears the equation text and updates the equation label.
    """
    global equation_text
    equation_label.set(' ')
    equation_text = ' '

w = Tk()

w.title("Calculator")
w.geometry("500x500")
equation_text = ''
equation_label = StringVar()

l = Label(w, textvariable=equation_label, font=('consolas', 20), bg='white', width=24, height=2)
l.pack()

f = Frame(w)
f.pack()

# Number Buttons
b1 = Button(f, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
b1.grid(row=0, column=0)
b2 = Button(f, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
b2.grid(row=0, column=1)
# ... (Buttons for other numbers)

# Operator Buttons
bp = Button(f, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
bp.grid(row=0, column=3)
bs = Button(f, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
bs.grid(row=1, column=3)
# ... (Buttons for other operators)

# Other Buttons
e = Button(f, text='=', height=4, width=9, font=35, command=equals)
e.grid(row=3, column=2)
c = Button(w, text='clear', height=4, width=12, font=35, command=clear)
c.pack()

w.mainloop()
