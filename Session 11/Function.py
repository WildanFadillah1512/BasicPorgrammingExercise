def calculate(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'divide':
        if y == 0:
            return "Error: Cannot divide by zero"
        else:
            return x / y
    else:
        return "Invalid operation"

def calculator():
    while True:
        print(f"""Select operation :
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit""")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice in ['1', '2', '3', '4']:
            operations = ['add', 'subtract', 'multiply', 'divide']
            operation = operations[int(choice) - 1]
            print("Result:", calculate(operation, num1, num2))
        else:
            print("Invalid input")

calculator()
