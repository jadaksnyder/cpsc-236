import csv

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
CSV_FILE = "monthly_sales.csv"

def read_sales():
    sales = {}
    with open(CSV_FILE, newline = '') as file:
        reader = csv.reader(file)
        for row in reader:
            month, amount = row
            sales[month] = int(amount)
    return sales

def write_sales(sales):
    with open(CSV_FILE, 'w', newline = '') as file:
        writer = csv.writer(file)
        for month, amount in sales.items():
            writer.writerow([month, amount])
            
def calculate_yearly_sales(sales):
    return sum(sales.values())

def calculate_monthly_average(sales):
    return round(sum(sales.values()) / len(sales), 2)

def show_monthly_sales(sales):
    print("Monthly Sales program\n")
    print("COMMAND MENU")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for month")
    print("exit - Exit program")
    print()
    command = input("Command: ").strip().lower()
    if command == "monthly":
        print("Monthly Sales:")
        for month, amount in sales.items():
            print(f"{month} - {amount}")
    elif command == "yearly":
        total_sales = calculate_yearly_sales(sales)
        average_sales = calculate_monthly_average(sales)
        print(f"Yearly total: {total_sales}")
        print(f"Monthly average: {average_sales}")
    elif command == "edit":
        month = input("Three-letter Month: ").strip().capitalize()
        if month not in MONTHS:
            print("Invalid month abbreviation.")
            return
        try:
            amount = int(input("Sales Amount: ").strip())
        except ValueError:
            print("Invalid sales amount.")
            return
        sales[month] = amount
        write_sales(sales)
        print(f"Sales amount for {month} was changed.")
    elif command == "Exit":
        print("Bye!")
        return
    else:
        print("Invalid command. Please try again.")
        
def main():
    sales = read_sales()
    while True:
        show_monthly_sales(sales)
        if input("\nPress enter to continue or type 'Exit' to quit: ").strip().lower() == "exit":
            break

if __name__ == "__main__":
    main()