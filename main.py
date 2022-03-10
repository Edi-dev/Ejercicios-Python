"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

from funciones import *


S = suma(2, 3)
R = resta(6, 4)
M = multiplica(5, 2)
D = division(8, 2)
print("El resultado de la suma es: ", S)
print("El resultado de la resta es: ", R)
print("El resultado de la multiplicación es: ", M)
print("El resultado de la división es: ", D)


# if  __name__  == '__operaciones__':
#    main()