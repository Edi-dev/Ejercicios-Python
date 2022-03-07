# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, "No es primo")
            return False
    print(num, "Es primo")
    return True

es_primo(25)