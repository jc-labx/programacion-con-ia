#! python

#
# Programación con Inteligencia Artificial - Actividad individual - Unidad 3
#
# Autor: Jaime Alberto Chica Betancourt
#
# Universidad de Investigación y Desarrollo – UDI
# Maestría en Ciencia de Datos e Inteligencia Artificial
# 7613 – Programación con IA
# Docente: Julián Andrés Ramirez Bautista
#
# Fecha de Entrega: 11 de Octubre de 2026
#


import os
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


class PricePredictor:

    """
    Responsabilidad: Entrenar y utilizar el modelo predictivo.

    Funciones principales:
        Construcción del pipeline de Machine Learning.
        Entrenamiento del modelo Random Forest.
        Evaluación mediante MAE, RMSE y R².
        Predicción de precios de nuevos laptops.
        Validación de entradas del usuario.
    """


    def __init__(self) -> None:

        """
        Inicializa el predictor de precios.
        """
        
        self.model = None
        self.X_test = None
        self.y_test = None
        self.predictions = None



    def train(self, df: pd.DataFrame) -> np.ndarray:

        """
        Construye el pipeline de Machine Learning y entrena el modelo predictivo.
        """

        # Elimina la variable objetivo y las columnas derivadas
        X = df.drop(
            columns=[
            "price",
            "price_segment"
            ]
            )


        """
        Elimina las características relacionadas con procesador y GPU.

        Se realizaron experimentos incorporando variables adicionales relacionadas con procesador y GPU. Sin embargo, la inclusión de estas características no mejoró el desempeño del modelo, observándose una disminución del coeficiente de determinación.

        Por este motivo se optó por conservar la versión más simple, que obtuvo un R² de 0.8446.
       """
        X = X.drop(
            columns=[
                "processor",
                "CPU",
                "GPU"
            ]
            )


        # Variable objetivo = Price
        y = df["price"]


        # Variables categóricas
        categorical_features = [
            "brand",
            "Ram_type",
            "ROM_type",
            "OS"
        ]

        # Variables numéricas: Utilizadas por el modelo.
        # Actualmente se procesan mediante remainder="passthrough"
        numeric_features = [
            "spec_rating",
            "Ram",
            "ROM",
            "display_size",
            "resolution_width",
            "resolution_height",
            "warranty",
            "total_pixels"
        ]

        # Codifica las variables categóricas y conserva las variables numéricas sin modificaciones
        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "categorical",
                    OneHotEncoder(handle_unknown="ignore"),
                    categorical_features
                )
            ],
            remainder="passthrough"
        )

        # Construye un pipeline que preprocesa los datos y entrena el modelo de regresión Random Forest
        self.model = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                (
                    "regressor",
                    RandomForestRegressor(
                        n_estimators=100,
                        random_state=42
                    )
                )
            ]
        )


        # Divide los datos en conjuntos de entrenamiento y prueba para evaluar el modelo
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42
        )

        # Entrena el modelo usando el conjunto de datos de entrenamiento
        self.model.fit(X_train, y_train)
        self.X_test = X_test
        self.y_test = y_test

        # Genera predicciones de precio para el conjunto de prueba
        predictions = self.model.predict(X_test)
        self.predictions = predictions

        return predictions


    def evaluate(self) -> dict:

        """
        Calcula las métricas de desempeño del modelo.
        """


        # Determina el mean absolute error
        mae = mean_absolute_error(
            self.y_test,
            self.predictions
        )

        # Determina el mean squared error
        rmse = np.sqrt(
            mean_squared_error(
                self.y_test,
                self.predictions
            )
        )

        # Determina el r2 score
        r2 = r2_score(
            self.y_test,
            self.predictions
        )

        return {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2
        }


    def get_valid_option(
            self,
            title: str,
            options: dict
        ) -> object:

            """
            Solicita y valida una opción seleccionada por el usuario.
            """

            while True:
                print(f"\n{title}")

                for key, value in options.items():
                    print(f"{key}. {value}")

                choice = input("\nOpción: ")
                if choice in options:
                    return options[choice]

                print("\nOpción inválida.")


    def predict_laptop(self) -> None:

        """
        Solicita características básicas de un portátil
        y genera predicciones para los datos proporcionados, utilizando el modelo entrenado.
        """

        os.system("cls")

        # Marca
        brands = {
            "1": "HP",
            "2": "Lenovo",
            "3": "Dell",
            "4": "Acer",
            "5": "Apple"
        }
        brand = self.get_valid_option("Seleccione la marca:",  brands)

        # RAM
        ram_options = {
            "1": 8,
            "2": 16,
            "3": 32,
            "4": 64
        }
        ram = self.get_valid_option("Memoria RAM:",  ram_options)


        # Tipo RAM
        ram_type_options = {
            "1": "DDR4",
            "2": "DDR5"
        }
        ram_type = self.get_valid_option("Tipo de RAM:",  ram_type_options)


        # Almacenamiento
        storage_options = {
            "1": 256,
            "2": 512,
            "3": 1024
        }
        rom = self.get_valid_option("Almacenamiento:",  storage_options)


        # Tipo almacenamiento
        rom_type_options = {
            "1": "SSD",
            "2": "HDD"
        }
        rom_type = self.get_valid_option("Almacenamiento:",  rom_type_options)


        # Sistema operativo
        os_options = {
        "1": "Windows 11 OS",
        "2": "Mac OS"
        }
        os_name = self.get_valid_option("Sistema Operativo:",  os_options)


        # Tamaño pantalla
        display_options = {
        "1": 13.3,
        "2": 14.0,
        "3": 15.6,
        "4": 16.0
        }
        display_size = self.get_valid_option("Tamaño de pantalla:",  display_options)


        # Resolución
        resolution_options = {
        "1": (1920, 1080),
        "2": (2560, 1600),
        "3": (3840, 2160)
        }
        width, height = self.get_valid_option("Resolución:",  resolution_options)


        # Nivel del equipo
        level_options = {
        "1": 60,
        "2": 75,
        "3": 90
        }
        spec_rating = self.get_valid_option("Nivel del equipo:",  level_options)


        # Configuración del laptop cuyo precio se va a predecir
        laptop = pd.DataFrame([
            {
                "brand": brand,
                "spec_rating": spec_rating,
                "Ram": ram,
                "Ram_type": ram_type,
                "ROM": rom,
                "ROM_type": rom_type,
                "display_size": display_size,
                "resolution_width": width,
                "resolution_height": height,
                "OS": os_name,
                "warranty": 1,
                "total_pixels": width * height
            }
        ])

        # Predice el precio del laptop de acuerod a la configuración seleccionada
        prediction = self.model.predict(laptop)
        print(f"\nPrecio estimado: " f"{prediction[0]:,.0f}")
        input("\nPresione una tecla para volver al menú principal.")


    def predict(self, data: pd.DataFrame) -> np.ndarray:

        """
        Predice a partir de la entrada en data.
        """

        return self.model.predict(data)
