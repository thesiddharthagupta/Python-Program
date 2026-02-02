#CoffeeKutira Restudent - Bill Calculator

print("Welcome to CoffeeKutira Restaurant Bill Calculator") 
print("Choose an operation:") 
print("1. Add - Calculate total bill (food cost + tax)") 
print("2. Subtract - Calculate discount amount (original bill - discounted bill)") 
print("3. Multiply - Calculate total for multiple identical orders") 
print("4. Divide - Split bill among customers") 

choose = int(input("Please choose any (1-4): "))
if choose == 1:
    foodCost = float(input("Enter Food Cost here: "))
    Tax = float(input("Enter Tax Amount: "))
    total_Bill = foodCost + Tax
    print("total bill is : ", total_Bill)

elif choose == 2:
    originalBill = float(input("Enter Original Bill here: "))
    Discount = float(input("ENter discount amt: "))
    final_bill = originalBill - Discount
    print("the discouted Bill is: ", final_bill)

elif choose == 3:
    cost = float(input("Enter cost per item: "))
    quantity = int(input("Enter quantity: "))
    total_cost = cost * quantity
    print("The identical order is: ", total_cost)

elif choose == 4:
    total_Bill = int(input("please Enter Bill amount to pay: "))
    customer = int(input("enter the no of customer to split the bill amt: "))
    if customer != 0:
        split_bill = total_Bill / customer
        print("the total split Bill is: ", split_bill)
    else:
        print("the number of customer cannt be zero")

else:
    print("invalid input, please select (1-4): ")

