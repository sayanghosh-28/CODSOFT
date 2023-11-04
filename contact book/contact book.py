import tkinter as tk
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title(" Contact Book")
root.geometry('750x630')
root.resizable(0, 0)
root.config(bg="#3DDEEC")

Label(root, text='CONTACT BOOK', font=("Noto Sans CJK TC", 15, "bold"), bg='Black', fg='White').pack(side=TOP, fill=X)

left_frame= Frame(root, bd=5,bg="#448489",width= 250, height= 630, cursor= "target")
left_frame.place(x=0,y=30)

middle_frame= Frame(root, bd=5,bg="#86EBF3",width= 250, height= 630, cursor= "target")
middle_frame.place(x=250,y=30)

right_frame= Frame(root, bd=5,bg="#CBFBFF",width= 250, height= 630, cursor= "target")
right_frame.place(x=500,y=30)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
contacts=[]
list1=[]
def search():
    search_text = entry5.get().lower()
    if search_text == "":
        messagebox.showerror("Error", "Search field cannot be empty.")
    else:
        for row in list1:
            if search_text == row[0] or search_text==row[1]:
                messagebox.showinfo("Contact Found", f"Name: {row[0]}\nPhone Number: {row[1]}\nEmail: {row[2]}\nAddress:{row[3]}")
                return
        messagebox.showinfo("Contact Not Found", f"No contact found with the name '{search_text}'.")


def add_contact():
    name=entry1.get()
    number=entry2.get()
    email=entry3.get()
    address=entry4.get(1.0,END)
    contacts.append([name,number])
    list1.append([name,number,email,address])
    print(list1)

    Select_set()
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(1.0,'end')
    
def update():
    name=entry1.get()
    number=entry2.get()
    email=entry4.get(1.0,END)
    address=entry3.get()
    
    contacts[int(listbox.curselection()[0])] = [entry1.get(), entry2.get()]
    list1[0][0]=name
    list1[0][1]=number
    list1[0][2]=email
    list1[0][3]=address
    #list1[int(listbox.curselection()[0])]=[entry1.get(),entry2.get(),entry3.get(),entry4.get()]
    Select_set()

    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    entry4.delete(1.0,'end')
    
def delete():
    if len(listbox.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contacts[int(listbox.curselection()[0])]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

def Select_set():
    contacts.sort()
    listbox.delete(0,END)
    for task in contacts :
        listbox.insert (END, task)
        #listbox.insert(END,number)
        listbox.insert('end',' ')
task=StringVar()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
label1=Label(left_frame, text='Name', bg="#448489", font="Helvetica 16 bold").place(relx=0.3, rely=0.03)

entry1=Entry(left_frame,width=25,font="Helvetica 15",bd=2)
entry1.place(x=7,y=50)
entry1.focus()

label2=Label(left_frame, text='Phone number', bg="#448489", font="Helvetica 16 bold").place(relx=0.2, rely=0.2)

entry2=Entry(left_frame,width=25,font="Helvetica 15",bd=2)
entry2.place(x=7,y=160)
entry2.focus()

label3=Label(left_frame, text='Email', bg="#448489", font="Helvetica 16 bold").place(relx=0.3, rely=0.37)

entry3=Entry(left_frame,width=25,font="Helvetica 15",bd=2)
entry3.place(x=7,y=260)
entry3.focus()

label4=Label(left_frame, text='Address', bg="#448489", font="Helvetica 16 bold").place(relx=0.3, rely=0.53)

entry4=Text(left_frame,width=25,height=5,font="Helvetica 15",bd=2)
entry4.place(x=7,y=360)
entry4.focus()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
label5=Label(middle_frame, text='Saved Contacts', bg="#86EBF3", font="Helvetica 20 bold underline").place(relx=0.1, rely=0.05)

listbox = Listbox(middle_frame, selectbackground='SkyBlue', bg='Gainsboro', font=('Helvetica', 12), height=20, width=25,cursor="hand2")
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand=scroller.set)
listbox.place(relx=0.05, rely=0.15)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
entry5=Entry(right_frame,width=25,font="Helvetica 13",bd=2)
entry5.place(x=7,y=50)
entry5.focus()

button1=Button(right_frame, text='Search', bg="#86EBF3", font="Helvetica 15 bold",command=search).place(relx=0.27, rely=0.13)
button2=Button(right_frame, text='Add Contact', bg="#86EBF3", font="Helvetica 15 bold",command=add_contact).place(relx=0.2, rely=0.3)
button3=Button(right_frame, text='Update', bg="#86EBF3", font="Helvetica 15 bold",command=update).place(relx=0.27, rely=0.45)
button4=Button(right_frame, text='Delete', bg="#86EBF3", font="Helvetica 15 bold",command=delete).place(relx=0.27, rely=0.6)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


root.mainloop()
