# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.

num = range(1, 101)

numOrdenado = sorted(num, reverse=True)
print(numOrdenado)
