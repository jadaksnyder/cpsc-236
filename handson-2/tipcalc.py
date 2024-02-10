print("Tip Calculator")
costmeal = float(input("Cost of the meal: "))
fifteen = costmeal * .15
twenty = costmeal * .20
twentyfive = costmeal * .25
amount15 = fifteen + costmeal
amount20 = twenty + costmeal
amount25 = twentyfive + costmeal

rounded_fifteen = round(fifteen,2)
rounded_twentyfive = round(twentyfive,2)
rounded_twenty = round(twenty,2)
rounded_costmeal = round(costmeal,2)
rounded_amount15 = round(amount15,2)
rounded_amount20 = round(amount20,2)
rounded_amount25 = round(amount25,2)

print("15%")
print(f"Tip Amount: {fifteen:.2f}")
print(f"Total Amount: {amount15:.2f}")

print("20%")
print(f"Tip Amount: {twenty:.2f}")
print(f"Total Amount: {amount20:.2f}")

print("25%")
print(f"Tip Amount: {twentyfive:.2f}")
print(f"Total Amount: {amount25:.2f}")

