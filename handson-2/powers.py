print("Table of Powers")

while True:
    startnum = int(input("Start number: "))
    stopnum = int(input("Stop number: "))
    
    if startnum < stopnum:
        break
    else:
        print("Please enter a start number that is less than the stop number.")

print("\nTable of Powers")
print("Number\tSquared\tCubed")
print("======\t=======\t=====")

for number in range(startnum, stopnum + 1):
    square = number ** 2
    cube = number ** 3
    print(f"{number}\t{square}\t{cube}")