# added correct shebang statement
# !/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
# added missing colon
while calc1 != "q":
    # changed print to raw_input = input(...)
    raw_input = input("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = raw_input
    if calc1 == "q":
        break
    calc1 = float(calc1)
    raw_input = input("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = raw_input
    if calc2 == "q":
        break
    calc2 = float(calc2)
    raw_input = input("Enter an operation to perform on the two operators (+ or -): ")
    operation = raw_input
    if operation == "+":
        # added "" around \n
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    # ifel => elif
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
