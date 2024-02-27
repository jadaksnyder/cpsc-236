#This function will display everything
def display():
    print("Feet and Meters Converter")
    print("Conversions Menu: ")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

#This function contains the conversions to calculate the user's input and uses a while loop to keep the program running
def convert():
    while True:
        choice = input("Select a conversion: ")
        if choice.lower() == "a":
            feet = float(input("Enter length in feet: "))
            meters = feet / 0.3048
            print(f"{feet} feet is equal to {meters} meters.")
        elif choice.lower() == "b":
            meters = float(input("Enter length in meters: "))
            feet = meters * 0.3048
            print(f"{meters} meters is equal to {feet} feet.")
        else:
            print("Invalid choice. Please enter 'a' or 'b'.")

        user_input = input("Would you like to continue? (y/n): ").lower()
        if user_input != "y":
            print("Bye!")
            break

display()
convert()
