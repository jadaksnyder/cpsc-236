def display():
    print("Currency Converter")
    
def convert():
    while True:
        usd_amount = float(input("Enter amount in USD: "))
        currency = usd_amount * 0.92
        print(f"{usd_amount} in EUR: {currency}")
        
        try_again = input("Continue? (y/n)").lower()
        if try_again != 'y':
            break
display()
convert()
    
    