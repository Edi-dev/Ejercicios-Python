# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

# Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

contador = 1

for contador in range(2, 8):
    if contador%2 != 0:
        print(contador, "es impar")