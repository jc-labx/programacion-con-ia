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

from pathlib import Path
import re

class ClasificadorRegex:

    # Clasificador con IA Simbólica

    PATRON_ALTA = r"\b(urgente|crítico|emergencia)\b"
    PATRON_MEDIA = r"\b(importante|pendiente|revisión)\b"

    def clasificar(self, texto):
        texto = texto.lower()

        if re.search(self.PATRON_ALTA, texto):
            return "ALTA"

        if re.search(self.PATRON_MEDIA, texto):
            return "MEDIA"

        return "BAJA"



class ClasificadorML:

    # Clasificador con Machine Learning

    def __init__(self):

        # Conjunto mínimo de entrenamiento
        ejemplos = [
            "urgente",
            "emergencia",
            "revisión",
            "pendiente",
            "boletín",
            "información general"
        ]

        # Etiquetas correspondientes
        etiquetas = [
            "ALTA",
            "ALTA",
            "MEDIA",
            "MEDIA",
            "BAJA",
            "BAJA"
        ]

        # Importa las librerias 
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.linear_model import LogisticRegression

        # Convierte texto a vectores numéricos
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(ejemplos)

        # Inicializa el modelo
        self.modelo = LogisticRegression()
        self.modelo.fit(X, etiquetas)


    def clasificar(self, texto):

        # Clasifica un texto de acuerdo a LogisticRegression
        X = self.vectorizer.transform([texto])
        return self.modelo.predict(X)[0]



def combinar(p1, p2):

    # Combina los resultados
    
    # Asigna valores a las prioridades
    prioridades = {
        "BAJA": 1,
        "MEDIA": 2,
        "ALTA": 3
    }

    # Selecciona la prioridad mas alta (reduce el riesgo que un mensaje importante sea clasificado con prioridad inferior)
    if prioridades[p1] >= prioridades[p2]:
        return p1
    else:
        return p2



class AnalizadorMensajes:

    # Analizador principal

    def __init__(self):
        # Inicializa las clases
        self.regex = ClasificadorRegex()
        self.ml = ClasificadorML()

    def procesar_carpeta(self, carpeta):

        # Imprime el encabezado
        print(
            f"{'Mensaje':<15}"
            f"{'IA Simbólica':<15}"
            f"{'Scikit-Learn':<15}"
            f"{'Final':}"
        )

        # Procesa los mensajes
        for mensaje in Path(carpeta).glob("*.txt"):
            with open(mensaje, encoding="utf-8") as f:
                texto = f.read()

            # Determina la prioridad usando clasificador Regex
            prioridad_regex = self.regex.clasificar(texto)
            # Determina la prioridad usando clasificador ML
            prioridad_ml = self.ml.clasificar(texto)
            # Determina la proridad mas alta entre las 2 prioridades anteriores
            prioridad_final = combinar(
                prioridad_regex,
                prioridad_ml
            )

            # Muestra los resultados
            print(
                f"{mensaje.name:<15}"
                f"{prioridad_regex:<15}"
                f"{prioridad_ml:<15}"
                f"{prioridad_final}"
            )


if __name__ == "__main__":

    # Ejecuta el analizador
    analizador = AnalizadorMensajes()
    analizador.procesar_carpeta("mensajes")