print("Change Calculator")

while True:
    cents = int(input("Enter number of cents (0-99): "))
    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickels = ((cents % 25) % 10) // 5
    pennies = ((cents % 25) % 10) % 5

    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")

    user_input = input("Would you like to continue? (y/n): ").lower()

    if user_input != "y":
        print("Bye!")
        break
