from art import logo


def add(n1, n2):
    n3 = n1 + n2
    return n3  # Return the calculated value

def subtract(s1, s2):
    s3 = s1 - s2
    return s3  # Return the calculated value

def multiply(m1, m2):
    m3 = m1 * m2
    return m3  # Return the calculated value

def divide(d1, d2):
    if d2 != 0:
        d3 = d1 / d2
        return d3  # Return the calculated value
    else:
        return "Error! Division by zero."  # Handle division by zero

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator_program():

    print(logo)
    # Ask the user to type the first number
    first_number = float(input("Enter first number: "))

    # Ask the user to choose which mathematical operator they want to use
    choice = input("+\n-\n*\n/\nPick an Operation: ")

    # Ask the user to type the second number
    second_number = float(input("Enter next number: "))

    # Perform the operation and print the result
    result = calculator[choice](first_number, second_number)

    # Print the result
    print(f"Result: {first_number} {choice} {second_number} = {result}")
    should_continue = True
    choice3 = input(f"Type 'y' to continue with {result} or 'n' to stop: ")
    while should_continue:
        select_operation = input("+\n-\n*\n/\nPick an Operation: ")
        next_number = float(input("Enter next number: "))
        result1 = calculator[select_operation](result, next_number)
        print(f"Result: {result} {select_operation} {next_number} = {result1}")
        choice2 = input(f"Type 'y' to continue with {result1} or 'n' to stop: ")

        if choice2 == "n":
            should_continue = False
            calculator_program()  # Start a new calculation
        elif choice2 == "exit":
            should_continue = False
            print("Calculator stopped.")
        elif choice2 != "y":
            print("Invalid input. Please type 'y', 'n', or 'exit'.")


calculator_program()




