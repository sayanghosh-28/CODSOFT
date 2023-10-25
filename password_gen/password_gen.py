import random
import string
plen=int(input("enter the desired size of your password"))

print("Chooise character combination\n 1.Digits \n 2.Letters\n 3.Digits and Letters")

s=[]
s1=[]
s2=[]
s.extend(string.ascii_lowercase)
s.extend(string.ascii_uppercase)
s.extend(string.digits)
s1.extend(string.digits)
s2.extend(string.ascii_lowercase)
s2.extend(string.ascii_uppercase)

choice=int(input("enter the type of character combination"))
x=[]
if(choice==1):
    print("Your password is: ")
    for i in range(plen):
        y=random.choice(s1)
        x.append(y)
    print("".join(x))
    #print("".join(random.sample(s1, plen)))
elif(choice==2):
        print("Your password is: ")
        for i in range(plen):
            y=random.choice(s2)
            x.append(y)
        print("".join(x))
        #print("".join(random.sample(s2, plen)))
elif(choice==3):
    print("Your password is: ")
    for i in range(plen):
        y=random.choice(s)
        x.append(y)
    print("".join(x))
    #print("".join(random.sample(s, plen)))
else:
    print("wrong input")
    
