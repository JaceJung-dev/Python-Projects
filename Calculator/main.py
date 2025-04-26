from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Cannot divide by zero"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    while True:
        try:
            first_num = float(input("What's the first number?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    is_continue = True

    while is_continue:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation:")
        while operation_symbol not in operations:
            operation_symbol = input(
                "You typed wrong operation, Pick an operation again."
            )

        while True:
            try:
                next_num = float(input("What's the next number?: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        result = operations[operation_symbol](first_num, next_num)

        print(f"{first_num} {operation_symbol} {next_num} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}. or type 'n' to start a new calculation, or 'q' to quit: "
        ).lower()

        if choice == "y":
            first_num = result
        elif choice == "n":
            is_continue = False
            calculator()
        elif choice == "q":
            return


calculator()
