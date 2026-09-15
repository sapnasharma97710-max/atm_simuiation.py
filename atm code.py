def atm():
    balance = 10000  
    print("Welcome to Python ATM!")

    while True:  
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            print(f"Current Balance: ₹{balance}")

        elif choice == '2':
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"Deposited: ₹{amount}")
                print(f"Updated Balance: ₹{balance}")
            else:
                print("Invalid amount!")

        elif choice == '3':
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount > balance:
                print("Insufficient balance! Withdrawal failed.")
            elif amount > 0:
                balance -= amount
                print(f"Withdrawn: ₹{amount}")
                print(f"Updated Balance: ₹{balance}")
            else:
                print("Invalid amount!")

        elif choice == '4':
            print(f"Final Balance: ₹{balance}")
            print("Thank you for using Python ATM. Bye!")
            break

        else:
            print("Invalid choice! Please select 1-4.")
atm()
