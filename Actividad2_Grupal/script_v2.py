#! python

#
# Programación con Inteligencia Artificial - Actividad grupal  Unidad 2
#
# Autor: Jaime Alberto Chica Betancourt
#
# Universidad de Investigación y Desarrollo – UDI
# Maestría en Ciencia de Datos e Inteligencia Artificial
# 7613 – Programación con IA
# Docente: Julián Andrés Ramirez Bautista
#
# Fecha de Entrega: 04 de Octubre de 2026
#

# Importar librerías necesarias
from typing import Tuple
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ============================================================
# 1. Cargar el dataset
# ============================================================

# Nombres de columnas del Adult Income Dataset
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

def load_data(filepath: str) -> pd.DataFrame:

    # MEJORA: Encapsulammiento y documentación de la carga de datos.
    
    """
    La funcion carga el dataset Adult Income desde un archivo .csv.
    Args:
        file_path: Ruta al archivo de datos.
    """

    try:
        # Trata de leer el archivo, gestiona excepciones si ocurren.
        df = pd.read_csv(
            filepath,
            header=None,
            names=columns,
            skipinitialspace=True
        )
        
    except Exception as error:
        print(f"Error: {error}")

    return df


# ============================================================
# 2. Mostrar información general
# ============================================================

def show_general_information(df: pd.DataFrame) -> None:
    
    # MEJORA: Funcion que despliega la informacion general.

    """Muestra la información general del dataset."""

    print("\n==============================")
    print("DIMENSIONES DEL DATASET")
    print("==============================")
    print(df.shape)

    print("\n==============================")
    print("TIPOS DE DATOS")
    print("==============================")
    print(df.dtypes)

    print("\n==============================")
    print("PRIMERAS FILAS")
    print("==============================")
    print(df.head())

    print("\n==============================")
    print("ESTADÍSTICAS DESCRIPTIVAS")
    print("==============================")
    print(df.describe())


# ============================================================
# 3. Limpieza básica
# ============================================================

def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    # MEJORA: Funcion de limpieza de datos.

    """Reemplaza '?' por valores nulos y elimina las filas incompletas."""

    df = df.copy()
    df.replace("?", pd.NA, inplace=True)
    df.dropna(inplace=True)
    return df


# ============================================================
# 4. Visualización de datos
# ============================================================

def show_data_charts(df: pd.DataFrame) -> None:

    # MEJORA: Funcion de graficacion.
    
    """
    La funcion muestra gráficos descriptivos y la matriz de confusión..
    Args:
        df: Dataframe en pandas
    """

    # Distribución de la variable objetivo
    plt.figure(figsize=(6, 4))
    df["income"].value_counts().plot(kind="bar")
    plt.title("Distribución de la variable objetivo")
    plt.xlabel("Ingreso")
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.show()

    # Distribución de edad
    plt.figure(figsize=(8, 4))
    df["age"].hist(bins=30)
    plt.title("Distribución de edades")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    # Horas trabajadas por semana
    plt.figure(figsize=(8, 4))
    df["hours_per_week"].hist(bins=30)
    plt.title("Horas trabajadas por semana")
    plt.xlabel("Horas")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


# ============================================================
# 5. Convertir variables categóricas en numéricas
# ============================================================

def encode_categorical_variables(df: pd.DataFrame) -> pd.DataFrame:

    # MEJORA: Funcion que codifica las variables categoricas
    
    # POSIBLE RIESGO: Esta función amerita análisis adicional y una revision adicional por parte de un especialista; pues es posible que la conversion de tipos de variables conlleve algún nivel de perdida de informacion 

    """Convierte las variables categóricas en valores numéricos."""

    df = df.copy()
    encoder = LabelEncoder()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = encoder.fit_transform(df[column])

    return df


# ============================================================
# 6. Preparar datos, entrenar y predecir
# ============================================================

def train_model(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:

    # MEJORA: Funcion que entrena el modelo

    """Divide los datos, entrena el modelo y devuelve la predicción."""

    if "income" not in df.columns:
        raise ValueError("La columna objetivo 'income' no existe.")

    X = df.drop("income", axis=1)
    y = df["income"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return y_test, y_pred


# ============================================================
# 7. Evaluación
# ============================================================

def evaluate_model(y_test: pd.Series, y_pred: pd.Series) -> Tuple[float, object]:

    # MEJORA: Funcion que evalua el modelo

    """Calcula la precisión y la matriz de confusión."""

    accuracy = accuracy_score(y_test, y_pred)
    confusionmatrix = confusion_matrix(y_test, y_pred)

    return accuracy, confusionmatrix


def show_results(accuracy: float, confusionmatrix: object) -> None:

    # MEJORA: Funcion que evalua el modelo

    """Muestra los resultados y la matriz de confusión."""

    print("\n==============================")
    print("PRECISIÓN DEL MODELO")
    print("==============================")
    print(f"Accuracy: {accuracy:.4f}")

    print("\n==============================")
    print("MATRIZ DE CONFUSIÓN")
    print("==============================")
    print(confusionmatrix)

    plt.figure(figsize=(5, 4))
    plt.imshow(confusionmatrix, cmap="Blues")
    plt.title("Matriz de confusión")
    plt.colorbar()
    plt.xlabel("Predicción")
    plt.ylabel("Valor real")

    for i in range(confusionmatrix.shape[0]):
        for j in range(confusionmatrix.shape[1]):
            plt.text(j, i, confusionmatrix[i, j], ha="center", va="center")

    plt.tight_layout()
    plt.show()


# ============================================================
# 8. Programa principal
# ============================================================

def main():

    # MEJORA: Funcion principal

    try:

        # Cargue del dataset
        df = load_data("adult.csv")

        # Mostrar informacion del dataset
        show_general_information(df)

        # Limpiar dataset
        df = clean_data(df)

        # Mostrar graficos
        show_data_charts(df)

        # Recodificar variables categoricas
        df = encode_categorical_variables(df)

        # Entrenar el modelo
        y_test, y_pred = train_model(df)

        # Evaluar el modelo
        accuracy, confusionmatrix = evaluate_model(y_test, y_pred)

        # Mostrar los resultados
        show_results(accuracy, confusionmatrix)

        print("\nModelo entrenado correctamente.")


    except Exception as error:
        # Manejo general de excepciones
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
