# Filename: interactive_widgets.py
'''
This code demonstrates the use of interactive widgets in a Tkinter application.
It includes various types of widgets such as a scale, listbox, color chooser, and text area.

The scale widget allows you to select a numeric value within a specified range.
The listbox widget displays a list of food items, and you can select multiple items.
The submit button retrieves the selected food items from the listbox.

The "Click me" button opens a color chooser dialog, allowing you to select a background color for the window.
The selected color is applied to the background of the window.

The text area widget provides a space to enter text, and the "Text Submit" button retrieves the entered text.

Feel free to interact with the widgets and explore their functionality!

'''
from tkinter import *
from tkinter import colorchooser

# Function to handle the submit button click event
def sub():
    food=[]
    for i in l.curselection():
        food.insert(i, l.get(i))
    print('You ordered:')
    for i in food:
        print(i)

# Function to handle the click event of the "click me" button
def click():
    color = colorchooser.askcolor()
    print(color[0])
    colorHex = color[1]
    print(colorHex)
    windows.config(bg=colorHex)

# Function to handle the text submit button click event
def textsub():
    inp = t.get('1.0', END)
    print(inp)

# Create the main window
windows = Tk()
windows.geometry('420x520')

# Create a scale widget
s = Scale(windows,
          from_=0,
          to=100,
          length=400,
          tickinterval=10)
s.place(x=0, y=0)

# Create a listbox widget
l = Listbox(windows,
            bg='white',
            font=('constantia', 35),
            width=20,
            selectmode=MULTIPLE)
l.place(x=120, y=0)
l.insert(1, 'pizza', 'soup', 'garlic bread', 'salad', 'chicken tikka')
l.config(height=l.size())

# Create a submit button
submitbutton = Button(windows, text='Submit', font=('arial', 20), command=sub)
submitbutton.place(x=120, y=300)

# Create a button to trigger color selection
b = Button(text='Click me', command=click)
b.place(x=650, y=0)

# Create a text area widget
t = Text(windows)
t.place(x=0, y=405)

# Create a text submit button
b2 = Button(text='Text Submit', command=textsub)
b2.place(x=0, y=500)

windows.mainloop()
