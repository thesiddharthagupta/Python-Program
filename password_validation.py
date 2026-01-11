'''Write a program to check login validation.'''

Correct_username = "siddharthgupta"
correct_password = "Siddgupta_27"

usrnam = input("Enter username: ")
psswed = input("Enter password: ")

if Correct_username == usrnam and correct_password == psswed:
    print("You Entered Corect password")
else:
    print("you entered Wrong Passwprd")
