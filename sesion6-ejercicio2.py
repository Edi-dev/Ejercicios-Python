# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llama Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

    def imprimir(self):
        print("Alumno: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota >= 3:
            print("El alumno aprobo la Nota")
        else:
            print("El alumno ha Reprobado")

alumno1 = alumno("Edison", 5)
alumno2 = alumno("Jairo", 2)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()