#! python

#
# Programación con Inteligencia Artificial - Actividad individual - Unidad 2
#
# Autor: Jaime Alberto Chica Betancourt
#
# Universidad de Investigación y Desarrollo – UDI
# Maestría en Ciencia de Datos e Inteligencia Artificial
# 7613 – Programación con IA
# Docente: Julián Andrés Ramirez Bautista
#
# Fecha de Entrega: 27 de Septiembre de 2026
#

import time, random
from monitor import monitor

@monitor
def entrenar_modelo():

    # Simula el proceso de entrenamiento

    # Inicio del proceso
    print("Iniciando entrenamiento...")

    for i in range(1, 6):

        # Simulo un tiempo variable de proceso espero una cantidad aleatoria de segundos
        time.sleep(random.randint(0, 5))

        # Muestro un indicador de progreso 
        print(f"{i*20}% completado...")


    # Fin del proceso
    print("Entrenamiento finalizado")

if __name__ == "__main__":
    entrenar_modelo()