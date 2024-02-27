
#def main():
    #number = int(input("Please enter an integer: "))
    #print(f"The factorial of {number} is {result}")
#def factorial(number):
    ###for i in range(2,number + 1):
        #result *= i
        #return result
    
#if __name__ == "__main__":
    #main()
def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

def main():
    number = int(input("Please enter an integer: "))
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()

    
        
        

        
    