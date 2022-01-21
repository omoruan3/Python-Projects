# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
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
    "_": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("select a number?\n"))

should_continue = True

while should_continue:
    def mathematical_operation(num1):
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the line above:\n")
        num2 = int(input("what is the next number?\n"))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        go_again = input(f"Type 'y' to continue with {answer}, or type 'n' to exit.:")
        if go_again == 'n':
            should_continue = False
            mathematical_operation(answer)

# operation_symbol = input("Pick another operation from the line above:\n")
# num3 = int(input("what is the next number?\n"))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer,num3)
#
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


mathematical_operation(num1)
