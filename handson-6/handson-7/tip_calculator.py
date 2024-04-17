def get_decimal(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Must be a valid decimal number: Please try again.")
            
def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Must be a valid integer. Please try again. ")
            
def calculate_tip(cost, tip_percent):
    tip = cost * (tip_percent /100)
    total_amount = cost +tip
    return tip, total_amount

def main():
    print("Welcome to the Tip Calculator!")
    cost_of_meal = get_decimal("Cost of meal: ")
    tip_percent = get_integer("Tip Percent: ")
    
    tip_amount, total_amount = calculate_tip(cost_of_meal, tip_percent)

    print("\nOUTPUT")
    print("Cost of meal:   {:.2f}".format(cost_of_meal))
    print("Tip percent:    {}%".format(tip_percent))
    print("Tip amount:     {:.2f}".format(tip_amount))
    print("Total amount:   {:.2f}".format(total_amount))

if __name__ == "__main__":
    main()
    