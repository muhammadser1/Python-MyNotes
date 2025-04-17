def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero")
        return num1
    return num1 / num2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    while True:
        num1 = float(input("What's the first number? "))
        current_result = num1

        while True:
            print("Available operations:", " ".join(operations.keys()))
            operator = input("Pick an operation: ")

            if operator not in operations:
                print("Invalid operation. Try again.")
                continue

            num2 = float(input("What's the next number? "))
            operation_func = operations[operator]
            current_result = operation_func(current_result, num2)

            print(f"Result: {current_result}")

            next_step = input(
                f"Type 'y' to continue with {current_result}, 'n' to start over, or 'q' to quit: ").lower()
            if next_step == 'n':
                break
            elif next_step == 'q':
                print("Calculator closed.")
                return


calculator()
