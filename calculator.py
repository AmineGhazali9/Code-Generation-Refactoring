def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_operation():
    operations = {
        "+": "add",
        "-": "subtract",
        "*": "multiply",
        "/": "divide",
    }
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in operations:
            return op
        print("Please choose a valid operation: +, -, *, or /.")


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            return None
        return a / b


def main():
    print("Basic Calculator")
    x = get_number("Enter the first number: ")
    y = get_number("Enter the second number: ")
    op = get_operation()

    result = calculate(x, y, op)
    if result is None:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {x} {op} {y} = {result}")


if __name__ == "__main__":
    main()
