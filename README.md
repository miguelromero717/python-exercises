# Python Exercises

This is a repository to expose some exercises to practice Python.

## Requirements

* `Python 3.7.x`

## Exercises
1. Develop a program that calculates the average of three notes, entered by keyboard, with these requirements 
    - The first note is worth 15% of the total. 
    - The second note is worth 35% of the total.
    - La tercera nota vale un 50% del total

    [Solution](calcula_nota_porcentual.py)
2. Develop a program that reads two numbers by keyboard and allows to choose between 3 options in a menu: 
    - Show a sum of the two numbers.
    - Show a subtraction of the two numbers (the first minus the second).
    - Show a multiplication of the two numbers.
    - If you do not enter a valid option, the program will inform you that it is not correct.

    [Solution](control_flujo_1.py)
3. Make a program that reads 2 numbers by keyboard and determines the following aspects (it is sufficient to show True or False):
    - If the two numbers are the same
    - If the two numbers are different
    - If the first is greater than the second
    - If the second is greater than or equal to the first
4. Using logical operators, determine if a user-entered text string has a length greater than or equal to 3 and in turn is less than 10 (it is sufficient to show True or False).
5. It carries out a program that complies with the following algorithm using, whenever possible, operators in assignment:
    - Saves the value 12345679 in a magical_number variable (without the 8)
    - Read another user_number on the screen, specify that it is between 1 and 9 (make sure it is a number)
    - Multiply the user_number by 9 in itself
    - Multiply themagic_number by the user_number itself
    - Finally it shows the final value of themagic_number per screen
6. Make a program that reads an odd number from the keyboard. If the user does not enter an odd number, the process must be repeated until it is entered correctly.
7. Performs a program that sums all even integers from 0 to 100.
8. Performs a program that asks the user how many numbers he wants to enter. Then he reads all the numbers and makes an arithmetic mean.
9. Make a program that asks the user for an integer from 0 to 9, and as long as the number is not correct repeat the process. Then you must check if the number is in the list of numbers and notify it.
    - numbers = [1, 3, 6, 9]
10. Using the range() function and the conversion to lists generates the following lists dynamically:
    - All numbers from 0 to 10 [0, 1, 2, ..., 10]
    - All numbers from -10 to 0 [-10, -9, -8, ..., 0]
    - All numbers even from 0 to 20 [0, 2, 4, ..., 20]
    - All odd numbers between -20 and 0 [-19, -17, -15, ..., -1]
    - All multiple numbers from 5 from 0 to 50 [0, 5, 10, ..., 50]  
11. Given two lists, you must generate a third one with all the elements that are repeated in them, but no element must be repeated in the new list.
12. Make a program that follows the instructions below:
    - Create a set called users with users Marta, David, Elvira, Juan and Marcos.
    - Create a set called administrators with administrators Juan and Marta.
    - Deletes John the administrator from the set of administrators.
    - Add Marcos as a new administrator, but don't delete him from the set of users.
    - Shows all users on the screen dynamically, also you must indicate each user is an administrator or not.
13. During the development of a small video game you are charged with configuring and balancing each class of playable character. Assuming that the basic statistic is 2, you must comply with the following conditions:
    - The knight has twice as much life and defense as a warrior.
    - The warrior has twice as much attack and reach as a knight.
    - The archer has the same life and attack as a warrior, but half his defense and twice his range.
    - It shows the properties of the three characters.
    - `caballero = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }`
    - `guerrero  = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }`
    - `arquero   = { 'vida':2, 'ataque':2, 'defensa': 2, 'alcance':2 }`
14. Format the following values to show the indicated result:
    - "Hello World" → Right aligned in 20 characters
    - "Hello World" → Truncation in the fourth character (index 3)
    - "Hello World" → Alignment to the center in 20 characters with truncation in the second character (index 1)
    - 150 → Format to 5 whole numbers filled with zeros
    - 7887 → Format to 7 whole numbers filled with spaces
    - 20.02 → Format to 3 integers and 3 decimal numbers


## Author
**Miguel Romero**