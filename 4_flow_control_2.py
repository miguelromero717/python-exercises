# Make a program that reads 2 numbers by keyboard and determines the following aspects (it is sufficient to show True or False):
#   - If the two numbers are the same
#   - If the two numbers are different
#   - If the first is greater than the second
#   - If the second is greater than or equal to the first

## The user enters the two values
number_one = int(input('Enter the first number '))
number_two = int(input('Enter the second number '))

## Inline validation
print("If the two numbers are the same. {}".format(number_one == number_two))
print("If the two numbers are different. {}".format(number_one != number_two))
print("If the first is greater than the second. {}".format(number_one > number_two))
print("If the second is greater than or equal to the first. {}".format(number_one <= number_two))

## Flow validation
if number_one > number_two:
    print("Number one is greater than number two")
elif number_two >= number_one:
    print("Number two is greater than number one") if number_two > number_one else print("Numbers are equals")
else:
    print("Numbers are different")
