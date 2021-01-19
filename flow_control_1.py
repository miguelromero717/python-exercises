# Make a program that reads two numbers on the keyboard and allows you to choose between 3 options on a menu:

# Show a sum of the two numbers
# Show a subtraction of the two numbers (the first minus the second)
# Show a multiplication of the two numbers
# If you do not enter a valid option, the program will inform you that it is not correct.

## The user enters the two values
numberOne = int(input('Enter the first number '))
numberTwo = int(input('Enter the second number '))

## The user selects an option menu to do some action with the numbers
option = int(input("""
    1. Sum 
    2. Subtraction
    3. Multiplication
"""))

## It is validated which option the user selected and the respective procedure is executed
if option == 1:
    res = numberOne + numberTwo
    print(f"Sum of values {res}")
elif option == 2:
    res = numberOne - numberTwo
    print(f"subtraction of values {res}")
elif option == 3:
    res = numberOne * numberTwo
    print(f"Multiplication of values {res}")