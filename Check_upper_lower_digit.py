'''
Write a program to check whether a character is:

uppercase

lowercase

digit

special character

'''

spam = input("Enter a charactor: ")
if spam.islower():
    print("the character is lower: ", spam)
elif spam.isupper():
    print("the  character is uppercase: ", spam)
elif spam.isdigit():
    print("The number is Digit:", spam)
else:
    print("the number is special character: ", spam)


