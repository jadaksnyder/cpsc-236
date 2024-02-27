def display():
    print("Sales tax Calculator")
    print("ENTER ITEMS (ENTER 0 TO END)")
    print("Cost of item: ")
    print("Total: ")
    print("Sales tax: ")
    print("Total after tax: ")

def calculate_sales_tax(cost):
    total = cost
    sales_tax = total * 0.06
    total_after_tax = total + sales_tax
    return total, sales_tax, total_after_tax

def convert():
    while True:
        customer_input = float(input("Cost of item (enter 0 to end): "))
        
        if customer_input == 0:
            print("Bye!")
            break

        total, sales_tax, total_after_tax = calculate_sales_tax(customer_input)

        print(f"Total: {total}")
        print(f"Sales tax: {sales_tax}")
        print(f"Total after tax: {total_after_tax}")

        user_input = input("Would you like to continue? (y/n): ").lower()
        if user_input != "y":
            print("Bye!")
            break

# Call the convert function to start the program
convert()
