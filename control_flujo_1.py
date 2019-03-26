# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

## El usuario ingresa los dos valores
numberOne = int(input('Ingrese el primer número '))
numberTwo = int(input('Ingrese el segundo número '))

## El usuario selecciona que hacer con los valores
option = int(input("""
    1. Sumar 
    2. Restar
    3. Multiplicar
"""))

## Se valida que opción selecciono el usuario
## y se ejecuta el respectivo procedimiento
if option == 1:
    res = numberOne + numberTwo
    print(f"La suma de los valores es {res}")
elif option == 2:
    res = numberOne - numberTwo
    print(f"La resta de los valores es {res}")
elif option == 3:
    res = numberOne * numberTwo
    print(f"La multiplicación de los valores es {res}")