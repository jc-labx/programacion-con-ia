#! python

#
# Programación con Inteligencia Artificial - Actividad individual - Unidad 1
#
# Autor: Jaime Alberto Chica Betancourt
#
# Universidad de Investigación y Desarrollo – UDI
# Maestría en Ciencia de Datos e Inteligencia Artificial
# 7613 – Programación con IA
# Docente: Julián Andrés Ramirez Bautista
#
# Fecha de Entrega: 20 de Septiembre de 2026
#

#
# Ejercicio 1
#
# Declare una variable con una temperatura en grados Celsius (float) y calcule su equivalente en Fahrenheit. 
# Muestre el resultado 𝐹=𝐶×1.8+32 indicando el tipo de dato final mediante la función type().
#

print(f"\nEjercicio 1:")

# Temperatura inicial (Celsius)
fTemp_Celsius = 25.5

# Temperatura calculada (Farenheit)
fTemp_Farenheit = (fTemp_Celsius * 1.8) + 32

# Imprimir la temperatura calculada
print(f"La temperatura {fTemp_Celsius} °C equivale a {fTemp_Farenheit} °F")

# Imprimir el tipo de variable de fTemp_Farenheit
print(f"El tipo de variable de fTemp_Farenheit es {type(fTemp_Farenheit).__name__}.\n")


#
# Ejercicio 2
#
# Cree una lista con 5 calificaciones parciales (list). 
# Agregue una nueva nota al final, elimine la nota más baja y calcule el promedio de las notas restantes.
#

print(f"Ejercicio 2:")

# Inicializar lista con 5 notas
lNotas = [2.5, 3, 5, 4, 1]

# Agregar nota al final
lNotas.append(3.5)

# Ordenar las notas
lNotasOrdenadas = list(sorted(lNotas))

# Variable intermedia para sumar las notas
fNotasSuma = 0

# Lista para almacenar las notas definitivas
lNotasDefinitivas = []

# Sumo el valor de las notas a partir de la segunda nota (ignoro la primera, porque es la más baja) hasta el final de la lista
for Nota in lNotasOrdenadas[1:]:
    fNotasSuma += Nota
    lNotasDefinitivas.append(Nota)

# Calculo el promedio dividiendo la suma de las notas entre el numero de notas menos una
fNotasPromedio = fNotasSuma / len(lNotasDefinitivas)
print(f"El promedio de las notas {lNotasDefinitivas} es {fNotasPromedio}.\n")


#
# Ejercicio 3
#
# Cree una tupla (tuple) con las coordenadas geográficas de su ciudad (latitud, longitud). 
# Intente modificar una de las coordenadas mediante asignación directa y registre en un comentario qué tipo de error genera Python y por qué ocurre.
#

print(f"Ejercicio 3:")

# Inicializo la latitud
Hamburgo_latitud = "53.55°N"

# Inicializo la longitud
Hamburgo_longitud = "9.99°E"

# Inicializo la tupla
tHamburgo_Coordenadas = (Hamburgo_latitud, Hamburgo_longitud)
print(f"Las coordenadas de Hamburgo son {tHamburgo_Coordenadas}.\n")

# Si intento modificar un valor de la tupla mediante asignación directa
#tHamburgo_Coordenadas[0] = "54.00°N"

# Obtengo el error
#TypeError: 'tuple' object does not support item assignment


#
# Ejercicio 4
#
# Ejericio 2 mejorado por IA
#

print(f"Ejercicio 4:")

# Inicializar lista con 5 notas
lNotas = [2.5, 3, 5, 4, 1]

# Agregar nota al final
lNotas.append(3.5)

# Creo una copia de la variable lNotas
lNotasDefinitivas = lNotas.copy()

# Elimino la nota mas baja
lNotasDefinitivas.remove(min(lNotasDefinitivas))

# Calculo el promedio
fNotasPromedio = sum(lNotasDefinitivas) / len(lNotasDefinitivas)

# Imprimo el promedio
print(f"El promedio de las notas {lNotasDefinitivas} es {fNotasPromedio}.\n")


#
# Ejercicio 5
#
# Cree una función llamada analizar_texto que reciba una cadena de texto y devuelva un diccionario con la cantidad de caracteres, cantidad de palabras y versión del texto en mayúsculas
#
# Nota: Intencionalmente no se agregaron comentarios al código fuente.
#

print(f"Ejercicio 5:")

def analizar_texto(texto):

    caracteres = len(texto)
    palabras = len(texto.split())
    mayusculas = texto.upper()

    diccionario = {
        "caracteres": caracteres,
        "palabras": palabras,
        "mayusculas": mayusculas
    }

    return diccionario

cadena = "Texto de prueba"
print(analizar_texto(cadena))


#
# Ejercicio 6
#
# Cree una función llamada analizar_texto que reciba una cadena de texto y devuelva un diccionario con la cantidad de caracteres, cantidad de palabras y versión del texto en mayúsculas
#
#

print(f"\nEjercicio 6:")

def analizar_texto(texto):
    """
    Analiza una cadena de texto y devuelve información básica.

    Parámetros:
        texto (str): Texto que se desea analizar.

    Retorna:
        dict: Diccionario con:
            - caracteres: cantidad de caracteres del texto.
            - palabras: cantidad de palabras del texto.
            - mayusculas: texto convertido a mayúsculas.
    """

    # Contar la cantidad de caracteres del texto
    caracteres = len(texto)

    # Separar el texto en palabras y contar cuántas hay
    palabras = len(texto.split())

    # Convertir todo el texto a letras mayúsculas
    mayusculas = texto.upper()

    # Crear un diccionario con los resultados obtenidos
    diccionario = {
        "caracteres": caracteres,
        "palabras": palabras,
        "mayusculas": mayusculas
    }

    # Devolver el diccionario con la información del análisis
    return diccionario


# Cadena de texto de prueba
cadena = "Texto de prueba"

# Ejecutar la función e imprimir el resultado
print(analizar_texto(cadena))


#
# Ejercicio 7
#
# Explique que hace el siguiente codigo

print(f"\nEjercicio 7:")

import math
import random


def procesar_lecturas(datos_raw):
    datos_limpios = list(set(datos_raw))
    lecturas_validas = []

    for valor in datos_limpios:
        if isinstance(valor, (int, float)) and valor >= 0:
            raiz = math.sqrt(valor)
            lecturas_validas.append(round(raiz, 2))

    return lecturas_validas


def generar_reporte(valores):
    if not valores:
        return {"estado": "sin_datos", "total": 0}

    conteo_altos = 0
    i = 0

    while i < len(valores):
        if valores[i] > 5.0:
            conteo_altos += 1
        i += 1

    resumen = {
        "total_procesados": len(valores),
        "promedio": round(sum(valores) / len(valores), 2),
        "maximo": max(valores),
        "minimo": min(valores),
        "alertas": conteo_altos
    }

    return resumen

muestras = [random.randint(-5, 50) for _ in range(15)]
muestras.extend([muestras[0], muestras[1]])

resultados = procesar_lecturas(muestras)
reporte_final = generar_reporte(resultados)

print("Datos de entrada:", muestras)
print("Resultado del procesamiento:", reporte_final)
