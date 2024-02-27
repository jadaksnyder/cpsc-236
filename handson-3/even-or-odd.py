def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
#The function determines whether the integer is odd or even
def main():
    print("Even or Odd Checker")
    user_input = int(input("Please enter an integer: "))
    result = evenOrOdd(user_input)
    print(f"This is an {result} number.")

if __name__ == "__main__":
    main()
