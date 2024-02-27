def display():
    print("Prime Number Checker")

def prime_num(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_factors(number):
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

while True:
    try:
        number = int(input("Please enter an integer between 1 and 5000: "))
        if 1 <= number <= 5000:
            if prime_num(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
                factor_list = calculate_factors(number)
                print(f"It has {len(factor_list)} factors: {', '.join(map(str, factor_list))}")
        else:
            print("Please enter an integer between 1 and 5000.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    
    try_again = input("Try again? (y/n): ").lower()
    if try_again != 'y':
        print("Bye!")
        break
