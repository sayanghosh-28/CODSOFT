import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)
root.configure(bg="#F6DDCC")

tasks=[]

def add_item():
    task_string=entry1.get()
    if(len(task_string)==0):
       messagebox.showinfo("to do list","Field is empty")
    else:
        tasks.append(task_string)
        listbox1.delete(0,'end')
        for task in tasks:
            listbox1.insert('end',task)
        entry1.delete(0,'end')
        

def delete_item():
    val=listbox1.get(listbox1.curselection())
    if val in tasks:
        tasks.remove(val)
        listbox1.delete(0,'end')
        for task in tasks:
            listbox1.insert('end',task)


        

def delete_all():
     message_box=messagebox.askyesno("delete","Do you want to delet all?")
     if(message_box==True):
         while(len(tasks)!=0):
             tasks.pop()

         listbox1.delete(0,'end')
         for task in tasks:
            listbox1.insert('end',task)



#mysql

#icon
img1=PhotoImage(file="images/to-do-list.png")
root.iconphoto(False,img1)

label1=Label(root,bg="#389C9F",width=60,height=5)
label1.pack()

img2=PhotoImage(file="images/dock.png")
Label(root,image=img2,bg="#32405b").place(x=30,y=25)

img3=PhotoImage(file="images/to-do-list1.png")
Label(root,image=img3,bg="#32405b").place(x=340,y=20)

label2=Label(root,text="To-Do-List",font="Impact 20 italic",fg="white",bg="#389C9F")
label2.place(x=130,y=20)

label3=Label(root,text="Hello, This is your to do list app",font="Lucida_Handwriting 15 bold",bg="#F6DDCC")
label3.place(x=10,y=100)
#frame
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=140)

task=StringVar()
entry1=Entry(frame,width=25,font="Helvetica 20",bd=2)
entry1.place(x=10,y=7)
entry1.focus()

button1=Button(root,text="ADD",font="Helvetica 17 bold",width=5,bg="#0FF377",fg="#fff",bd=0,command=add_item)
button1.place(x=155,y=193)

#listbox

frame1=Frame(root,bd=3,width=500,height=280,bg="#389C9F")
frame1.pack(pady=(160,0))

listbox1=Listbox(frame1,font=('Helvetica',13),width=40,height=15,bg="#389C9F",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox1.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT ,fill=BOTH)

listbox1.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=Listbox.yview)

#delete
img6=PhotoImage(file="images/delete.png")
Button(root,image=img6,bd=0,command=delete_item).place(x=55,y=555)
label4=Label(root,text="Delete",font="Helvetica 13",bg="#F6DDCC")
label4.place(x=53,y=600)

img4=PhotoImage(file="images/delete_all (2).png")
Button(root,image=img4,bd=0,command=delete_all).place(x=305,y=555)
label5=Label(root,text="Delete All",font="Helvetica 13",bg="#F6DDCC")
label5.place(x=285,y=600)

img5=PhotoImage(file="images/exit.png")
Button(root,image=img5,bd=0,command=root.destroy).place(x=182,y=590)




root.mainloop()




