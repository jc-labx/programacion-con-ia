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
        Inicializa la clase.
        """
        
        self.model = None
        self.X_test = None
        self.y_test = None
        self.predictions = None



    def train(self, df: pd.DataFrame) -> np.ndarray:

        """
        Entrena el modelo usando el dataframe.

        Se realizaron experimentos incorporando variables adicionales relacionadas con procesador y GPU. Sin embargo, la inclusión de estas características no mejoró el desempeño del modelo, observándose una disminución del coeficiente de determinación.

        Por este motivo se optó por conservar la versión más simple, que obtuvo un R² de 0.8446.
        """

        X = df.drop(
            columns=[
            "price",
            "price_segment"
            ]
            )

        X = X.drop(
            columns=[
                "processor",
                "CPU",
                "GPU"
            ]
            )        

        y = df["price"]

        categorical_features = [
            "brand",
            "Ram_type",
            "ROM_type",
            "OS"
        ]

        """
        Variables numéricas utilizadas por el modelo.
        Actualmente se procesan mediante remainder="passthrough".
        """
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

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        self.X_test = X_test
        self.y_test = y_test
        self.predictions = predictions

        return predictions


    def evaluate(self) -> dict:

        """
        Evalúa el modelo.
        """

        mae = mean_absolute_error(
            self.y_test,
            self.predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                self.y_test,
                self.predictions
            )
        )

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
            Valida las entradas de las caracteristicas del laptop.
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
        y estima su precio utilizando el modelo entrenado.
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

        prediction = self.model.predict(laptop)

        print(f"\nPrecio estimado: " f"{prediction[0]:,.0f}")
        input("\nPresione una tecla para volver al menú principal.")


    def predict(self, data: pd.DataFrame) -> np.ndarray:

        """
        Predice a partir de la entrada en data.
        """

        return self.model.predict(data)
