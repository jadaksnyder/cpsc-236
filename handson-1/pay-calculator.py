hours = float(input("How many hours have you worked?"))
pay = float(input("What is your pay rate?"))

grosspay = hours * pay
taxrate = 18
taxs = grosspay * (taxrate/100)
thpay = grosspay - taxs 
print("Pay Check Calculator")
print()
print(f"Hours Worked: {hours}")
print(f"Hourly Pay Rate: {pay}")
print()
print(f"Gross Pay: {grosspay}")
print(f"Tax Rate: {taxrate}%")
print(f"Tax Amount: {taxs}")
print(f"Take Home Pay: {thpay}")
#i like python
