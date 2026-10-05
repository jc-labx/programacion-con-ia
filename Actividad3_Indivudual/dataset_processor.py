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

from typing import Dict
import pandas as pd

class DatasetProcessor:

    """
    Responsabilidad:  Preparar y transformar los datos antes del entrenamiento.

    Funciones principales:
        Carga del dataset CSV.
        Limpieza de columnas innecesarias.
        Conversión de RAM y almacenamiento a valores numéricos.
        Creación de nuevas características.
        Segmentación de precios.
        Preparación final del dataset para Machine Learning.
    """

    def __init__(self, file_path: str) -> None:

        """Inicializa la clase."""

        self.file_path = file_path
        self.df = None


    def load_data(self) -> pd.DataFrame:

        """
        Carga el archivo CSV.
        """

        try:
            self.df = pd.read_csv(self.file_path)
            return self.df

        except FileNotFoundError:
            print(f"\nERROR: No se encontró " f"el archivo:\n{self.file_path}")
            raise SystemExit(1)

        except pd.errors.EmptyDataError:
            print("\nERROR: El archivo CSV está vacío.")
            raise SystemExit(1)

        except Exception as ex:
            print(f"\nERROR inesperado al cargar el dataset:\n{ex}")
            raise SystemExit(1)


    def get_summary(self) -> dict:

        """
        Obtiene estadísticas descriptivas del dataset
        """

        return {
            "records": len(self.df),
            "columns": len(self.df.columns),
            "min_price": self.df["price"].min(),
            "max_price": self.df["price"].max(),
            "avg_price": self.df["price"].mean(),
            "brands": self.df["brand"].nunique(),
            "segments": self.df["price_segment"].value_counts().to_dict()
        }


    def remove_unused_columns(self) -> pd.DataFrame:

        """Define las columnas que el modelo ignora."""

        unnamed_columns = [
            col
            for col in self.df.columns
            if col.startswith("Unnamed")
        ]

        columns_to_drop = unnamed_columns + [
            "name"
        ]

        self.df = self.df.drop(
            columns=columns_to_drop,
            errors="ignore"
        )

        return self.df


    def clean_ram(self) -> pd.DataFrame:

        """Convierte '16GB' -> 16."""

        self.df["Ram"] = (
            self.df["Ram"]
            .str.replace("GB", "", regex=False)
            .astype(int)
        )

        return self.df



    def clean_storage(self) -> pd.DataFrame:

        """
        Convierte:
        512GB -> 512
        1TB -> 1024
        """

        def convert_storage(value):

            value = str(value).upper()

            if "TB" in value:
                number = float(value.replace("TB", ""))
                return int(number * 1024)

            if "GB" in value:
                number = float(value.replace("GB", ""))
                return int(number)

            return None

        self.df["ROM"] = self.df["ROM"].apply(convert_storage)

        return self.df


    def create_resolution_feature(self) -> pd.DataFrame:

        """Crea los píxeles totales como nueva característica."""

        self.df["total_pixels"] = (
            self.df["resolution_width"]
            * self.df["resolution_height"]
        )

        return self.df


    def create_price_segment(self) -> pd.DataFrame:

        """Crea los segmentos de precio."""

        self.df["price_segment"] = pd.cut(
            self.df["price"],
            bins=[
                0,
                50000,
                100000,
                200000,
                float("inf")
            ],
            labels=[
                "Budget",
                "Mid-Range",
                "Premium",
                "Ultra Premium"
            ]
        )

        return self.df


    def fill_missing_values(self) -> pd.DataFrame:

        """Completa valores faltantes."""

        self.df = self.df.fillna({
            "warranty": 0
        })

        return self.df


    def prepare_dataset(self) -> pd.DataFrame:

        """Prepara el dataset."""

        self.remove_unused_columns()
        self.clean_ram()
        self.clean_storage()
        self.create_resolution_feature()
        self.create_price_segment()
        self.fill_missing_values()

        return self.df
