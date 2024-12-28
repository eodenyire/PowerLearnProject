# Basic Calculator Program

# Ask the user for input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")
elif operation == "-":
    result = number1 - number2
    print(f"{number1} - {number2} = {result}")
elif operation == "*":
    result = number1 * number2
    print(f"{number1} * {number2} = {result}")
elif operation == "/":
    if number2 != 0:  # Prevent division by zero
        result = number1 / number2
        print(f"{number1} / {number2} = {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
