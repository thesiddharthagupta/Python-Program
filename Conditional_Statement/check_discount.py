'''
Write a program to calculate discount:

Total > 500 → 10% discount

Else → No discount
'''


total = float(input("Enter the total amount: "))

if total > 500:
    discount = total * 0.10
    final_amount = total - discount
    print(f"Discount applied: {discount:.2f}")
    print(f"Final amount to pay: {final_amount:.2f}")
else:
    print("No discount applied.")
    print(f"Final amount to pay: {total:.2f}")
