import tkinter
from tkinter import *
import random

root=Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("650x650+650+100")
root.resizable(False,False)
root.configure(bg="#F9D298")

your_score=0
computer_score=0
user=" "
comp=" "

def button_disable():
   button1.config(state= "disabled")
   button2.config(state= "disabled")
   button3.config(state= "disabled")


def end():
    x=""
    if computer_score<your_score:
        x="user"
    elif computer_score>your_score:
        x="Computer"
    else:
        x="Nobody"
    label16=Label(root,text=f"So the Winner is {x}",font="Algerian 20",bg="#38F19F",fg="red")
    label16.place(x=150,y=550)
    button_disable()


def points():
    text_to_scores.delete("1.0","end")
    text_to_scores.insert(END,f"  {your_score}                                                                          {computer_score}")


def rock():
    global your_score,your_choice
    global computer_score,Comp_choice
    your_choice="rock"
    Comp_choice=random.choice(['rock','scissors','paper'])
    label13.config(text="rock")
    label14.config(text=Comp_choice)
    if Comp_choice=="paper":
        computer_score+=1
    if Comp_choice=="scissors":
        your_score+=1
    points()


def paper():
    global your_score,your_choice
    global computer_score,Comp_choice
    your_choice="paper"
    Comp_choice=random.choice(['rock','scissors','paper'])
    label13.config(text="paper")
    label14.config(text=Comp_choice)
    if Comp_choice=="scissors":
        computer_score+=1
    if Comp_choice=="rock":
        your_score+=1
    points()

def scissors():
    global your_score,your_choice
    global computer_score,Comp_choice
    your_choice="scissors"
    Comp_choice=random.choice(['rock','scissors','paper'])
    label13.config(text="scissors")
    label14.config(text=Comp_choice)
    if Comp_choice=="rock":
        computer_score+=1
    if Comp_choice=="paper":
        your_score+=1
    points()


img1=PhotoImage(file="images/download.png")
root.iconphoto(False,img1)

label1=Label(root,bg="#38F19F",width=100,height=6)
label1.pack()

label2=Label(root,text="Hello, Welcome to \n rock-paper-scissors game",bg="#38F19F",font="Algerian 20 bold",fg='red')
label2.place(x=110,y=20)

img2=PhotoImage(file="images/download(1).png")
Label(root,image=img2,bg="#38F19F").place(x=560,y=20)

label3=Label(root,text="Rules:-",bg="#F9D298",font="Helvetica 20 bold underline")
label3.place(x=50,y=110)

label4=Label(root,text="1.Rock beats Scissors",bg="#F9D298",font="Helvetica 21 italic")
label4.place(x=200,y=110)

label5=Label(root,text=" 2.Paper beats Rocks",bg="#F9D298",font="Helvetica 21 italic")
label5.place(x=195,y=140)

label6=Label(root,text="3.Scissors beats Paper",bg="#F9D298",font="Helvetica 21 italic")
label6.place(x=200,y=170)

labelframe= LabelFrame(root, text= "",labelanchor= "n",bd=5,bg="#F9D288",width= 625, height= 600, cursor= "target")
labelframe.place(x=10,y=210)

label7=Label(root,text="Make Your Choice",font= ('Century 20 bold'),bg="#D4C944",width=15)
label7.place(x=200,y=230)

img3=PhotoImage(file="images/rock_1 (2).png")
#Label(root,image=img3).place(x=50,y=280)
button1=Button(root,text="",image=img3,command=rock)
button1.place(x=50,y=280)

img4=PhotoImage(file="images/paper (1).png")
#Label(root,image=img4).place(x=290,y=280)
button2=Button(root,text="",image=img4,command=paper)
button2.place(x=290,y=280)

img5=PhotoImage(file="images/scissors (1).png")
#Label(root,image=img5).place(x=500,y=270)
button3=Button(root,text="",image=img5,command=scissors)
button3.place(x=500,y=270)

label8=Label(root,text="Rock",bg="#F9D298",font="Helvetica 15 bold")
label8.place(x=55,y=370)


label9=Label(root,text="Paper",bg="#F9D298",font="Helvetica 15 bold")
label9.place(x=290,y=370)

label10=Label(root,text="Scissors",bg="#F9D298",font="Helvetica 15 bold")
label10.place(x=500,y=370)

label11=Label(root,text="Your choice",bg="#F9D298",fg="blue",font="Algerian 20 bold underline")
label11.place(x=30,y=410)

label12=Label(root,text="Computer choice",bg="#F9D298",fg="blue",font="Algerian 20 bold underline")
label12.place(x=360,y=410)

label13=Label(root,text="You",bg="#F9D298",fg="violet",font="Berlin_Sans_FB 20 bold")
label13.place(x=30,y=450)

label14=Label(root,text="Comp",bg="#F9D298",fg="violet",font="Berlin_Sans_FB 20 bold")
label14.place(x=450,y=450)

label15=Label(root,text="VS",bg="#F9D298",fg="black",font="Berlin_Sans_FB 20 bold")
label15.place(x=260,y=450)

text_to_scores=Text(root,height=1,width=50,font="Helvetica 15")
text_to_scores.place(x=50,y=500)

end=Button(root,text="End Game",height=1,bg="red",font="Helvetica 15 bold",command=end)
end.place(x=260,y=600)

root.mainloop()
