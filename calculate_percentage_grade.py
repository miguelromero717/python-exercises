# Desarrollar un programa que calcule la nota final de acuerdo 
# a las siguientes condiciones:

# La primera nota vale un 15% del total
# La segunda nota vale un 35% del total
# La tercera nota vale un 50% del total

# Las tres notas deben ser ingresadas por el usuario

## El usuario ingresa las tres notas
nota_1 = int(input("Digite la nota 1: "))
nota_2 = int(input("Digite la nota 2: "))
nota_3 = int(input("Digite la nota 3: "))

# Calculo del porcentaje de cada nota
nota_final_1 = (nota_1 * 0.15)
nota_final_2 = (nota_2 * 0.35)
nota_final_3 = (nota_3 * 0.5)

nota_final = nota_final_1 + nota_final_2 + nota_final_3

print("La nota final es {}".format(str(nota_final)))