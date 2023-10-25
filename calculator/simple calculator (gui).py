# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:16:01 1022

@author: hp
"""

from tkinter import *
#from tkinter import messagebox

root=Tk()
root.title("Simple Calcultor")
root.configure(background="#66BFBF")
root.geometry("500x500")



def press(number):
    global expression
    expression=expression+str(number)
    input_text.set(expression)

def clear():
    global expression
    expression=""
    input_text.set("")

def equal():
    global expression
    global result
    result=str(eval(expression))
    input_text.set(result)
    expression=""
    
def delete():
    delete(END,0)

input_text=StringVar()
expression=""
    
e=Entry(root,textvariable=input_text,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

number=StringVar()

button1 = Button(root, text=' 1 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(1), height=5, width=10)
button1.grid(row=4, column=0)
 
button2 = Button(root, text=' 2 ', fg='black', bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(2), height=5, width=10)
button2.grid(row=4, column=1)

button3 = Button(root, text=' 3 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(3), height=5, width=10)
button3.grid(row=4, column=2)

button4 = Button(root, text=' 4 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(4), height=5, width=10)
button4.grid(row=3, column=0)
 
button5 = Button(root, text=' 5 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(5), height=5, width=10)
button5.grid(row=3, column=1)
 
button6 = Button(root, text=' 6 ', fg='black', bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(6), height=5, width=10)
button6.grid(row=3, column=2)
 
button7 = Button(root, text=' 7 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(7), height=5, width=10)
button7.grid(row=2, column=0)
 
button8 = Button(root, text=' 8 ', fg='black',bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(8), height=5, width=10)
button8.grid(row=2, column=1)
 
button9 = Button(root, text=' 9 ', fg='black', bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(9), height=5, width=10)
button9.grid(row=2, column=2)
 
button0 = Button(root, text=' 0 ', fg='black', bg='light blue',activeforeground='orange',font=("Helvetica",10,'bold'),command=lambda: press(0), height=5, width=10)
button0.grid(row=5, column=0)
 
plus = Button(root, text=' + ', fg='black', bg='gold',font=("Helvetica",10,'bold'),command=lambda:press("+"), height=5, width=10)
plus.grid(row=5, column=3)
 
minus = Button(root, text=' - ', fg='black', bg='gold',font=("Helvetica",10,'bold'),command=lambda:press("-"), height=5, width=10)
minus.grid(row=4, column=3)
 
multiply = Button(root, text=' * ', fg='black', bg='gold',font=("Helvetica",10,'bold'),command=lambda:press("*"), height=5, width=10)
multiply.grid(row=3, column=3)
 
divide = Button(root, text=' / ', fg='black', bg='gold',font=("Helvetica",10,'bold'),command=lambda:press("/"), height=5, width=10)
divide.grid(row=2, column=3)
 
equal = Button(root, text=' = ', height=5, width=10, fg='black', bg='gold',font=("Helvetica",10,'bold'),command=equal)
equal.grid(row=5, column=2)
 
clear = Button(root, text='Clear',  height=5, width=10,fg='black', bg='gold',font=("Helvetica",10,'bold'),command=clear)
clear.grid(row=1, column=0)
 
Decimal= Button(root, text='.', fg='black', bg='gold',command=lambda:press("."),font=("Helvetica",10,'bold'), height=5, width=10)
Decimal.grid(row=5, column=1)

modulus=Button(root,text=' % ',fg='black', bg='gold',command=lambda:press("%"),font=("Helvetica",10,'bold'), height=5, width=10)
modulus.grid(row=1,column=2)

delete=Button(root,text='D',fg='black', bg='gold',command=delete,font=("Helvetica",10,'bold'), height=5, width=10)
delete.grid(row=1,column=3)
root.mainloop()