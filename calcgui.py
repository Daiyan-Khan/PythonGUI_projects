from tkinter import *

def button_press(num):
    global equation_text
    equation_text=equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    try:
        global equation_text
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except SyntaxError:
        equation_label.set('Syntax error')
    except ZeroDivisionError:
        equation_label.set('arithmetic error')
def clear():
    global equation_text
    equation_label.set(' ')
    equation_text=' '
w=Tk()

w.title("Calculator")
w.geometry("500x500")
equation_text=''
equation_label=StringVar()

l=Label(w,textvariable=equation_label,font=('consolas', 20), bg='white',width=24, height=2)
l.pack()

f=Frame(w)
f.pack()

b1=Button(f,text=1,height=4,width=9, font =35, command=lambda: button_press(1) )
b1.grid(row=0,column=0)
b2=Button(f,text=2,height=4,width=9, font =35, command=lambda: button_press(2) )
b2.grid(row=0,column=1)
b3=Button(f,text=3,height=4,width=9, font =35, command=lambda: button_press(3) )
b3.grid(row=0,column=2)
b4=Button(f,text=4,height=4,width=9, font =35, command=lambda: button_press(4) )
b4.grid(row=1,column=0)
b5=Button(f,text=5,height=4,width=9, font =35, command=lambda: button_press(5) )
b5.grid(row=1,column=1)
b6=Button(f,text=6,height=4,width=9, font =35, command=lambda: button_press(6) )
b6.grid(row=1,column=2)
b7=Button(f,text=7,height=4,width=9, font =35, command=lambda: button_press(7) )
b7.grid(row=2,column=0)
b8=Button(f,text=8,height=4,width=9, font =35, command=lambda: button_press(8) )
b8.grid(row=2,column=1)
b9=Button(f,text=9,height=4,width=9, font =35, command=lambda: button_press(9) )
b9.grid(row=2,column=2)
b0=Button(f,text=0,height=4,width=9, font =35, command=lambda: button_press(0) )
b0.grid(row=3,column=0)

bp=Button(f,text='+',height=4,width=9, font =35, command=lambda: button_press('+'))
bp.grid(row=0,column=3)
bs=Button(f,text='-',height=4,width=9, font =35, command=lambda: button_press('-') )
bs.grid(row=1,column=3)
bm=Button(f,text='*',height=4,width=9, font =35, command=lambda: button_press('*') )
bm.grid(row=2,column=3)
bd=Button(f,text='/',height=4,width=9, font =35, command=lambda: button_press('/') )
bd.grid(row=3,column=3)
e=Button(f,text='=',height=4,width=9, font =35, command=equals)
e.grid(row=3,column=2)
decimal=Button(f,text='.',height=4,width=9, font =35, command=lambda: button_press('.') )
decimal.grid(row=3,column=1)
c=Button(w,text='clear',height=4,width=12, font =35, command=clear )
c.pack()


w.mainloop()