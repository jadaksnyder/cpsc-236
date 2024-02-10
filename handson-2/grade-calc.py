print("Letter Grade Converter")

while True:
    numgrade = int(input("Enter numerical grade: "))

    if numgrade >= 88:
        lettergrade = "A"
    elif numgrade >= 80 and numgrade <= 87:
        lettergrade = "B"
    elif numgrade >= 67 and numgrade <= 79:
        lettergrade = "C"
    elif numgrade >= 60 and numgrade <= 66:
        lettergrade = "D"
    else:
        lettergrade = "F"

    print(f"Letter grade: {lettergrade}")

    user_input = input("Would you like to continue? (y/n): ").lower()

    if user_input != "y":
        print("Bye!")
        break
