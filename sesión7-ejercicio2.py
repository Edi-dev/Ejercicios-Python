"""En este segundo ejercicio tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""

import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')


import time
import datetime

fecha_actual =  print(time.strftime('%c'))

hora_actual = datetime.datetime.now(fecha_actual)
hora_salida = datetime.datetime(2022, 3, 16, 19, 00, 00)

if hora_actual < hora_salida:
    tiempoRestante = hora_salida - hora_actual
    print('Aun no es hora de salir faltan: ', tiempoRestante, 'para terminar la jornada')
elif hora_actual > hora_salida:
    print("Ya puedes salir son las: ", hora_actual)
else:
    print("Fin del programa")



