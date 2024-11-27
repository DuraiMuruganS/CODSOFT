# Function to add two numbers
def add(x, y):
    return x + y
# Function to subtract two numbers
def subtract(x, y):
    return x - y
# Function to multiply two numbers
def multiply(x, y):
    return x * y
# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
# Taking input from the user
    choice = input("Enter choice (1/2/3/4): ")
# Validating the choice
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please choose a valid operation.")
        return
# Taking the numbers as input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
# Performing the calculation based on the user's choice
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
# Run the calculator
calculator()
