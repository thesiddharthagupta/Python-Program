'''Write a program to check whether a triangle is valid.'''

a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("this is valid trangle ")
else:
    print("this is not valid trangle")
    
