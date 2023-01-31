# Calculator
import art

print(art.logo)


# Add
def add(n1, n2):
    return n1 + n2


# Sutract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# For formatting string.
str_symbols = ""

# Ask user for two numbers and the operator.
for operation_symbol in operations:
    str_symbols += operation_symbol + " "
    # This concatenate the operations for display


def calculator():
    num1 = float(input("n1: "))

    is_running = True
    while is_running:

        operator_choice = input(f"Operation ( {str_symbols}): ")
        num2 = float(input("n2: "))

        # Calculate stores the function according to user choice. (Add, subtract, etc)
        calculate = operations[operator_choice]

        # Execute chosen function and store to a "answer" variable.
        answer = calculate(num1, num2)

        # Print (no shot)
        print(f"{num1} {operator_choice} {num2} = {answer}")

        user_choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' for new calculation: "
        )
        if user_choice in ["y", "n"]:
            if user_choice == "y":
                num1 = answer
                is_running = True
            else:
                is_running = False
                calculator()


calculator()
