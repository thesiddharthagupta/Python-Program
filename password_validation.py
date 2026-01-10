'''Write a program to check login validation.'''

Correct_username = "thesiddharthagupta"
correct_password = "Siddgupta_27"

username = input("Enter username: ")
password = input("Enter password: ")

if Correct_username == username and correct_password == password:
    print("You Entered Corect password")
else:
    print("you entered Wrong Passwprd")
