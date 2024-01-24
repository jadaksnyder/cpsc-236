# This program will allow a student to create a registration form
name = input("What is your first name?")
lastname = input("What is your last name?")
year = input("What is your birth year?")
print("Registration Form ")
print()
# printing the users input
print(f"First Name: {name}")
print(f"Last Name: {lastname}")
print(f"Birth Year: {year}")
# printing their password
print()
print(f"Welcome {name} {lastname}!")
print("Your registration is complete!")
print(f"Your temporary password is: {name}*{year}")
