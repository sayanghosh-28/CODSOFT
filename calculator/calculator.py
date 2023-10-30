def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def float(x,y):
    return x%y
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number: "))
print("selection operation")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.division")
print("5.modulo division")
choice=int(input("select operation 1/2/3/4/5  : "))

if(choice==1):
        print(num1, "+", num2, "=", addition(num1, num2))
elif(choice==2):
        print(num1, "-", num2, "=", subtraction(num1, num2))
elif(choice==3):
        print(num1, "*", num2, "=", multiply(num1, num2))
elif(choice==4):
        print(num1, "/", num2, "=", division(num1, num2))
elif(choice==5):
    print(num1,"%",num2,"=",modulus(num1,num2))
else:
    print("invalid user")
    
