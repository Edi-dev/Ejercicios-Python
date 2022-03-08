"""
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
- Color
- Ruedas
- Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
- Velocidad
- Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

"""

class Vehiculo:
    color = None
    Ruedas = 4
    Puertas = 4  

class Coche(Vehiculo):
    Velocidad = 0
    Cilindrada = 900

    def __init__(self):
        self.color = "Verde"
        self.velocidad = 80


c = Coche()
print("la Velocidad aumento a: ", c.velocidad)
print("El color del coche es: ", c.color)

