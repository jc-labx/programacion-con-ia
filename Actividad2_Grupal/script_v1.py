# ============================================================
# Adult Income Dataset - Predicción de ingresos >50K
# ============================================================

# Importar librerías necesarias
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

# El archivo original suele venir en formato .data
# Se cargan manualmente los nombres de las columnas
df = pd.read_csv(
    "adult.csv",
    header=None,
    names=columns,
    skipinitialspace=True
)

# ============================================================
# 2. Mostrar información general
# ============================================================

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

# Reemplazar '?' por valores nulos
df.replace("?", pd.NA, inplace=True)

print("\n==============================")
print("VALORES FALTANTES")
print("==============================")
print(df.isnull().sum())

# Eliminar filas con valores faltantes
df.dropna(inplace=True)

# ============================================================
# 4. Visualización de datos
# ============================================================

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

encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = encoder.fit_transform(df[column])

# ============================================================
# 6. Separar variables predictoras y objetivo
# ============================================================

X = df.drop("income", axis=1)
y = df["income"]

# ============================================================
# 7. Dividir entrenamiento y prueba
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ============================================================
# 8. Entrenar el modelo
# ============================================================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# ============================================================
# 9. Realizar predicciones
# ============================================================

y_pred = model.predict(X_test)

# ============================================================
# 10. Evaluación
# ============================================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("PRECISIÓN DEL MODELO")
print("==============================")
print(f"Accuracy: {accuracy:.4f}")

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)

print("\n==============================")
print("MATRIZ DE CONFUSIÓN")
print("==============================")
print(cm)

# Visualización de la matriz de confusión
plt.figure(figsize=(5, 4))
plt.imshow(cm, cmap="Blues")
plt.title("Matriz de confusión")
plt.colorbar()
plt.xlabel("Predicción")
plt.ylabel("Valor real")

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()

# ============================================================
# 11. Resultados finales
# ============================================================

print("\nModelo entrenado correctamente.")
print("Proceso finalizado.")