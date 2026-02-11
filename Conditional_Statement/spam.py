n1 = int(input("ENter a number: "))
n2 = int(input("ENter a number: "))
n3 = int(input("ENter a number: "))

if n1 > n2 and n1 > n3:
    print("the Greater number is :", n1)
elif n2 > n1 and n2 > n3:
    print("greater number is : ", n2)
elif n3 > n1 and n3 > n2:
    print("the greater number is : ", n3)
else:
    print("Invalid number, please Enter again!")

    