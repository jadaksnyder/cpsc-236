def display():
    print("Simple ATM System")

def check_balance(balance):
    print("Choose an option: ")
    print("1. Check Balance")
    print("2. Withdraw money")
    print("3. Exit")
    user_choice = int(input("Enter choice: "))

    if user_choice == 1:
        print(f"Your current balance is ${balance}.")
    elif user_choice == 2:
        withdrawal = int(input("Enter amount to withdraw: "))
        if withdrawal > balance:
            print("Insufficient funds!")
        else:
            total = balance - withdrawal
            print(f"Transaction successful. Your new balance is ${total}.")
    elif user_choice == 3:
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please choose a valid option.")


balance = 1000 
display()
check_balance(balance)
