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
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Visualizer:

    """
    Responsabilidad: Generar y visualizar resultados gráficos.

    Funciones principales:
        Distribución de precios.
        Precio por marca.
        Segmentación por rango de precio.
        Comparación entre valores reales y predichos.
        Apertura de gráficas desde el dashboard.
    """

    def __init__(self) -> None:

        """
        Inicializa la clase
        """

        sns.set_style("whitegrid")
        self.output_dir = "outputs"

        os.makedirs(
            self.output_dir,
            exist_ok=True
        )

    def plot_price_distribution(self, df: pd.DataFrame) -> None:

        """
        Grafico de la distribución de precio
        """

        plt.figure(figsize=(10, 6))
        sns.histplot(
            df["price"],
            bins=30,
            kde=True
        )

        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Count")
        plt.tight_layout()

        plt.savefig(f"{self.output_dir}/price_distribution.png")

        plt.close()



    def plot_price_by_brand(self, df: pd.DataFrame) -> None:

        """
        Grafico de la distribución de precio por marca
        """

        top_brands = (
            df["brand"]
            .value_counts()
            .head(10)
            .index
        )

        filtered_df = (
            df[df["brand"].isin(top_brands)]
        )

        plt.figure(figsize=(12, 6))

        sns.boxplot(
            data=filtered_df,
            x="brand",
            y="price"
        )

        plt.title("Price by Brand")
        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(f"{self.output_dir}/price_by_brand.png")

        plt.close()


    def plot_feature_importance(
        self,
        feature_names,
        importances
    ):

        """
        Grafico del precio por característica
        """

        import pandas as pd

        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importances
        })

        importance_df = (
            importance_df
            .sort_values(
                by="Importance",
                ascending=False
            )
        )

        plt.figure(figsize=(10, 6))

        sns.barplot(
            data=importance_df,
            x="Importance",
            y="Feature"
        )

        plt.title("Feature Importance")
        plt.tight_layout()

        plt.savefig(f"{self.output_dir}/feature_importance.png")

        plt.close()


    def plot_actual_vs_predicted(
        self,
        y_test: pd.Series,
        predictions: np.ndarray
    ) -> None:

        """
        Grafico del precio actual vs precios predecidos
        """

        plt.figure(figsize=(8, 8))

        sns.scatterplot(
            x=y_test,
            y=predictions
        )

        min_value = min(
            min(y_test),
            min(predictions)
        )

        max_value = max(
            max(y_test),
            max(predictions)
        )

        plt.plot(
            [min_value, max_value],
            [min_value, max_value],
            color="red",
            linestyle="--"
        )

        plt.title("Actual Price vs Predicted Price")
        plt.xlabel("Actual Price")
        plt.ylabel("Predicted Price")
        plt.tight_layout()

        plt.savefig(f"{self.output_dir}/actual_vs_predicted.png")

        plt.close()


    def plot_price_segments(self, df: pd.DataFrame) -> None:

        """
        Grafico de los segmentos de precio
        """

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=df,
            x="price_segment",
            order=[
                "Budget",
                "Mid-Range",
                "Premium",
                "Ultra Premium"
            ]
        )

        plt.title("Laptop Distribution by Price Segment")
        plt.xlabel("Price Segment")
        plt.ylabel("Number of Laptops")

        plt.tight_layout()

        plt.savefig(f"{self.output_dir}/price_segments.png")

        plt.close()


    def generate_all(
        self,
        df: pd.DataFrame,
        y_test: pd.Series,
        predictions: np.ndarray
    ) -> None:

        """
        Genera todas las gráficas
        """

        self.plot_price_distribution(df)

        self.plot_price_by_brand(df)

        self.plot_price_segments(df)

        self.plot_actual_vs_predicted(
            y_test,
            predictions
        )


    def open_chart(self, option: str) -> None:

        """
        Abre una gráfica utilizando el visor
        por defecto del sistema operativo.
        """

        charts = {
            "1": "price_distribution.png",
            "2": "price_by_brand.png",
            "3": "price_segments.png",
            "4": "actual_vs_predicted.png"
        }

        if option not in charts:
            print("\nOpción inválida.")
            return

        file_path = os.path.join(
            self.output_dir,
            charts[option]
        )

        os.startfile(file_path)