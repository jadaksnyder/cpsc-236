# def display():
#     print("Simple ATM System")
#     print("Choose an option:")
#     print("1. Check Balance")
#     print("2. Withdraw Money")
#     print("3. Exit")
    
# def user_input():
#     balance = 1000
#     while True:
#         display()
#         choice = input("Enter choice: ")
#         if choice.isdigit():
#             choice = int(choice)
#         else:
#             print("Please enter a valid choice.")
#             continue
            
        
        
#         if choice == 1:
#             print(f"Your current balance is ${balance}")
#         elif choice == 2:
#             withdrawal = float(input("Enter amount to withdraw: "))
#             if balance - withdrawal < 0:
#                 print("Insufficient funds.")
#             else:
#                 balance = balance - withdrawal
#                 print(f"Transaction successful. Your new balance is ${balance}.")
#         elif choice == 3:
#             print("Goodbye!")
#             break

# user_input()
        
# foods = []
# print(foods)
# foods.append("bananas")
# print(foods)
# foods.remove("bananas")
# print(foods)

foods = []
def show_fav_food():
    print(foods)
    
def add_fav_food():
    foods.append()
    
def remove_fav_food():
    foods.remove()

def fav_foods():
    while True:
    print("Favorite Foods Tracker")
    choice = input("Choose an option: ")
    

    
        
        
        
        