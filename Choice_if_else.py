# Menu-driven program using if–elif–else

def discount_calculator():
    total = float(input("Enter total amount: "))
    if total > 500:
        discount = total * 0.10
        final_amount = total - discount
        print(f"Discount applied: ₹{discount:.2f}")
        print(f"Final amount: ₹{final_amount:.2f}")
    else:
        print("No discount applied.")
        print(f"Final amount: ₹{total:.2f}")

def login_validation():
    correct_username = "admin"
    correct_password = "12345"
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful ✅")
    else:
        print("Login failed ❌")

def ticket_price():
    age = int(input("Enter your age: "))
    if age < 12:
        price = 100
    elif age <= 17:
        price = 150
    elif age <= 59:
        price = 200
    else:
        price = 120
    print(f"Your ticket price is: ₹{price}")

# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Calculate Discount")
    print("2. Login Validation")
    print("3. Ticket Price")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        discount_calculator()
    elif choice == "2":
        login_validation()
    elif choice == "3":
        ticket_price()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")