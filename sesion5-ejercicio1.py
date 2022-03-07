# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

base = float(input("Digite la base: "))
altura = float(input("Digite la altura: "))

area = base * altura / 2 
print("El area de el el triangulo es ", area)

from math import pi

radio = float(input("Digite el radio del circulo: "))

areaCirculo = pi * radio ** 2 
print("el area del circulo es: ", areaCirculo)