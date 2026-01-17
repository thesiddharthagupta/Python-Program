'''
Write a program to check a students grade:

≥ 90 → A

≥ 75 → B

≥ 60 → C

else → Fail

'''

check = int (input("Enter grade of student: "))
if check >= 90:
    print("you have scored grade A", check)
elif check >= 75:
    print("You have scored grade B", check)
elif check >= 60:
    print("You have scored grade C", check)

else:
    print("sorry u have faild")
