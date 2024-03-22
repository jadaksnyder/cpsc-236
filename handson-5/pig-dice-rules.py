with open('rules.txt', 'r') as file:
    rules = file.read() #reads the lines from the file
    
    print("Pig Dice Rules:")
    print(rules)