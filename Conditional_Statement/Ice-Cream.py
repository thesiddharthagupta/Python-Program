'''You're managing an ice cream parlour. Write a program that shows the menu, takes customer orders, Asks "Do you want to order more?" after each order and calculates total bill with 8% tax'''

# Ice Cream Parlour Billing Program 
print("Welcome to the Ice Cream Parlour!") 
print("----------- MENU -----------") 
print("1. Vanilla Scoop - 40") 
print("2. Chocolate Scoop - 50") 
print("3. Strawberry Scoop - 45") 
print("4. Butterscotch Scoop - 55") 
print("-----------------------------")

total_bill = 0
orderMore = "yes"

while orderMore.lower() == "yes":
    choose = int(input("Enter Your choise (1-4): "))
    quantity = int(input("Enter quantity of items: "))

    if choose == 1:
        total_bill += 40 * quantity     #total_bill = total_bill + 40 * quantity
        print("You have Ordered Vanila Scope X", quantity)

    elif choose == 2:
        total_bill += 50 * quantity      #total_bill = total_bill 50 * quantity
        print("You have Ordered chocolet scoope X", quantity)

    elif choose == 3:
        total_bill += 45 * quantity
        print("You have Ordered stavery scoopeX", quantity)

    elif choose == 4:
        total_bill += 55 * quantity
        print("You have Ordered Butter scoope X", quantity)
    else:
        print("Invalid chooice!, please select (1-4)")
    
    orderMore = input("Do you want to ordermore? (yes/no): ")

tax = total_bill * 0.08
final_bill = total_bill + tax

print("----------------")
print("total Bill before tax: ",total_bill)
print("tax amt is: ", tax)
print("total Bill with tax to pay: ", final_bill)



