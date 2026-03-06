print("=== Shubham's Calculator ===")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter operation (+,-,*,/):")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid operation!")
    result = None

if result is not None:
    print(f"Result: {num1} {operation} {num2} = {result}")