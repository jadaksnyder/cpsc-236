FILENAME = "monthly_sales.txt"

def write_sales(sales):
    with open(FILENAME, "w") as file:
        for month, amount in sales.items():
            file.write(f"{month},{amount}\n")

def read_sales():
    sales = {}
    with open(FILENAME, "r") as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 2:
                month, amount = parts
                sales[month] = float(amount)
    return sales



def view(sales):
    month = input("Three-letter Month: ").lower()
    if month in sales:
        print(f"Sales amount for {month} is {sales[month]:,.2f}.")
    else:
        print("Invalid three-letter month.")
        
def view_yearly_summary(sales):
    total = sum(sales.values())
    monthly_average = total / len(sales)

    print(f"Yearly total: {total:,.2f}")
    print(f"Monthly average: {monthly_average:,.2f}")
    print()

def edit(sales):
    month = input("Three-letter Month: ").lower()
    if month in sales:
        amount = float(input("Sales Amount: "))
        sales[month] = amount
        write_sales(sales)
        print(f"Sales amount for {month} was modified.")
        print()
    else:
        print("Invalid three-letter month.")
        print()

def display_menu():
    print("COMMAND MENU")
    print("view   - View sales for specified month")
    print("edit   - Edit sales for specified month")
    print("totals - View sales summary for year")
    print("exit   - Exit program")
    print()

def main():
    print("Monthly Sales program")
    print()

    sales = read_sales()
    display_menu()
    while True:
        command = input("Command: ").lower()
        if command == "view":
            month = input("Three-letter Month: ").lower()
            if month in sales.keys:
                print(f"Sales amount for {month} is {sales[month]:,.2f}.")
            else:
                print("Invalid three-letter month.")
        elif command == "edit":
            edit(sales)
        elif command == "totals":
            view_yearly_summary(sales)
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")
            print()
    print("Bye!")

if __name__ == "__main__":
    main()