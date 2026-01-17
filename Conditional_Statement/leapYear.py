'''
Write a program to check whether a year is a leap year

'''

year = int(input("ENter the year: "))
if year % 400 == 0:
    print("the year is leap Year: ", year)
elif year % 100 == 0:
    print("the year is not leap year: ", year)
elif year % 4 == 0:
    print("the year is leap year: ", year)
else:
    print(" the year is not leap year")

    