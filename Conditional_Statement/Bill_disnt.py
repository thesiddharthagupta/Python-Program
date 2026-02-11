print("Welcome to the Shopping Mall Billing System")

numItems = int(input("Enter number of items to buy: "))
totalBill = 0

print("\nItemized Receipt:")

for i in range(1, numItems + 1):
    itemPrice = float(input("Enter price of item " + str(i) + ": "))
    totalBill += itemPrice

print("\nTotal before discount: ", totalBill)

if totalBill > 100:
    discount = totalBill * 0.10
    totalBill -= discount
    print("10% discount applied: ", discount)
else:
    print("No discount applied.")

print("Final Bill Amount: ", totalBill)
