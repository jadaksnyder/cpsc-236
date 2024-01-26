miles = int(input("Enter Miles: "))
mph = int(input("Enter Miles per Hour: "))

#calculating total minutes and hours
total_minutes = miles * 60 // mph
hours = total_minutes //mph
minutes = total_minutes % mph
#printing results
print("Travel Time Calculator")
print("Estimated Travel Time")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")