'''
Write a program to find the largest of three numbers
'''

spam1 = int(input("Enter 1st number : "))
spam2 = int(input("Enter 2st number : "))
spam3 = int(input("Enter 3st number : "))
if spam1 > spam2 and spam1 > spam3:
    print("the greater number is : ", spam1)
elif spam2 > spam3 and spam2 > spam1:
    print("the greater number is: ", spam2)
elif spam3 > spam1 and spam3 >  spam2:
    print("the greater number is: ", spam3)
else:
    print("equal")




'''
another method: # pythonn have build in feature of MAX--

spam1 = int(input("Enter 1st number : "))
spam2 = int(input("Enter 2nd number : "))
spam3 = int(input("Enter 3rd number : "))

print("The greatest number is:", max(spam1, spam2, spam3))

'''