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

import time
from datetime import datetime
from functools import wraps

def monitor(func):

    """
    Decorador que registra el tiempo de ejecución y captura posibles excepciones.
    @wraps: Preservar los metadatos de la función original
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        # Caracter de separacion
        sSeparador = "*"
        
        # Tiempo de inicio de la funcion
        tInicio = time.time()
        fInicio = datetime.now()
        
        # Muestra el mensaje en el momento que la funcion inicia
        print(f"{func.__name__} {sSeparador} {fInicio.strftime('%Y/%m/%d-%H:%M:%S')} {sSeparador} Inicio")

        try:
            # Ejecuta la funcion 
            resultado = func(*args, **kwargs)
            
            # Tiempo de inicio de la funcion
            tFin = time.time()
            fFin = datetime.now()
            
            # Muestra el mensaje en el momento que la funcion termina
            print(f"{func.__name__} {sSeparador} {fFin.strftime('%Y/%m/%d-%H:%M:%S')} {sSeparador} Fin \n{func.__name__} {sSeparador} Tiempo de ejecucion {tFin - tInicio:.2f} segundos")
            
            # Devuelve el resultado de la funcion
            return resultado

        except Exception as error:
            
            # Ocurre un error

            # Tiempo en el que ocurre el error
            tError = time.time()
            fError = datetime.now()

            # Muestra el mensaje de error en el momento que ocurre
            print(f"{func.__name__} {sSeparador} {fError.strftime('%Y/%m/%d-%H:%M:%S')} {sSeparador} Error: {error}")

            # Eleva el error
            raise

    return wrapper
