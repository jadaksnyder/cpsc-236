def display():
    print("Prime Number Checker")
    print("Please enter a number between 1 and 5000: ")
    
def calculate_prime_number(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
        return True
    

def convert():
    while True:
        user_input = int(input("Please enter an integer between 1 and 5000: "))
        if user_input < 1 or user_input > 5000:
            print("Invalid integer. Please try again.")
            continue
        if calculate_prime_number(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is not a prime number.")
            print(f"It has {len([i for i in range(1, user_input + 1) if user_input % i == 0])} factors.")
            
        user_input = input("Try again? (y/n): ").lower()
        if user_input != "y":
            print("Bye!")
            
if __name__ == "__main__":
    display()
    convert()            
        
    