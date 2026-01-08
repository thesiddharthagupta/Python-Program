# Program to determine ticket price based on age


age = int(input("Enter your age: "))


if age < 12:
    price = 100
elif age <= 17:
    price = 150
elif age <= 59:
    price = 200
else:
    price = 120

# Output result
print(f"Your ticket price is: {price}")