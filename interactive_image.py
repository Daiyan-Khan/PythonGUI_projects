# File Name: interactive_image.py
# This script implements an interactive image application using the tkinter library in Python.
# It allows the user to drag and move a label on the window, control its movement using arrow keys,
# display a digital clock that updates every second, and show an image on the window.

from tkinter import *
from time import *

def something(event):
    # Function to handle key press event
    print("you pressed: " + event.keysym)
    l.config(text=event.keysym)

def drag(event):
    # Function to handle dragging of the label
    l.startX = event.x
    l.startY = event.y

def drag_motion(event):
    # Function to handle motion during dragging
    x = l.winfo_x() - l.startX + event.x
    y = l.winfo_y() - l.startY + event.y
    l.place(x=x, y=y)

def up(event):
    # Function to move the label up
    x = l2.winfo_x()
    y = l2.winfo_y() - 10
    l2.place(x=x, y=y)

def down(event):
    # Function to move the label down
    x = l2.winfo_x()
    y = l2.winfo_y() + 10
    l2.place(x=x, y=y)

def left(event):
    # Function to move the label left
    x = l2.winfo_x() - 10
    y = l2.winfo_y()
    l2.place(x=x, y=y)

def right(event):
    # Function to move the label right
    x = l2.winfo_x() + 10
    y = l2.winfo_y()
    l2.place(x=x, y=y)

def update():
    # Function to update the clock label every second
    t_string = strftime('%I:%M:%S %p')
    timelabel.config(text=t_string)
    timelabel.after(1000, update)

# Create the main window
w = Tk()
w.geometry('420x420')

# Bind keys to their respective functions
w.bind('<w>', up)
w.bind('<s>', down)
w.bind('<a>', left)
w.bind('<d>', right)

# Create and place the draggable label
r = PhotoImage(file='Coding\Python\SAMPLE\Racecar.png')
l = Label(w, font=('Arial', 10), bg='red', width=10, height=5)
l.place(x=0, y=0)
l.bind("<Button-1>", drag)
l.bind("<B1-Motion>", drag_motion)

# Create and update the clock label
timelabel = Label(w, font=("times new roman", 20), bg='black', fg='white')
timelabel.pack()
update()

# Create and place the image label
l2 = Label(w, image=r)
l2.place(x=0, y=300)

# Start the main event loop
w.mainloop()
