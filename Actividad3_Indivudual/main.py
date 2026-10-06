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
from dataset_processor import DatasetProcessor
from price_predictor import PricePredictor
from visualizer import Visualizer


def header(header_str: str) -> None:

    """
    Imprime un encabezado
    """

    os.system("cls")

    print("\n" + "=" * 40)
    print(header_str)
    print("=" * 40)

    return


def show_dashboard_menu():

    """
    Menu dashboard
    """
    
    header("DASHBOARD")
    
    print("1. Distribución de precios")
    print("2. Precio por marca")
    print("3. Segmentación por precio")
    print("4. Precio real vs predicho")
    print("5. Volver")

    return input("\nSeleccione una opción: ")


def get_dashboard_option():

    """
    Valida la entrada del menu dashboard
    """

    while True:
        option = show_dashboard_menu()
        if option in ["1","2","3","4","5"]:
            return option
        
        print("\nSeleccione una opción válida.")
        input("\nPulse ENTER para continuar...")


def show_menu() -> str:

    """
    Menu principal
    """

    header("PREDICCION DE PRECIOS DE LAPTOPS")
    print("1. Resumen del dataset")
    print("2. Mostrar métricas del modelo")
    print("3. Visualizaciones y dashboard")
    print("4. Predecir precio de un laptop")
    print("5. Salir")

    return input("\nSeleccione una opción: ")


def get_main_menu_option() -> str:

    """
    Valida la entrada del menu
    """

    while True:
        option = show_menu()

        if option in ["1","2","3","4","5"]:
            return option

        print("\nSeleccione una opción válida.")
        input("\nPulse ENTER para continuar...")



def main() -> None:

    print("Cargando el dataset.")
    processor = DatasetProcessor("data.csv")

    processor.load_data()

    print("Preparando el dataset.")
    df = processor.prepare_dataset()


    predictor = PricePredictor()

    print("Entrenando el modelo.")
    predictor.train(df)

    print("Evaluando el modelo.")
    metrics = predictor.evaluate()

    visualizer = Visualizer()

    print("Generando visualizaciones.")
    visualizer.generate_all(
        df,
        predictor.y_test,
        predictor.predictions
    )

    while True:

        os.system('cls')
        option = get_main_menu_option()

        if option == "1":

            summary = processor.get_summary()

            header("RESUMEN DEL DATASET")

            print(f"Número de registros: " f"{summary['records']}")
            print(f"Número de columnas: " f"{summary['columns']}")
            print(f"Precio mínimo: " f"{summary['min_price']:,.0f}")
            print(f"Precio máximo: " f"{summary['max_price']:,.0f}")
            print(f"Precio promedio: " f"{summary['avg_price']:,.2f}")
            print(f"Cantidad de marcas: " f"{summary['brands']}")

            print("\nSegmentación de precios:")
            for segment, count in summary["segments"].items():
                print(f" {segment}: {count}")

            input("\nPresione una tecla para volver al menú principal.")


        elif option == "2":

            header("METRICAS DEL MODELO")
            
            print(f"MAE  : {metrics['MAE']:.2f}")
            print(f"RMSE : {metrics['RMSE']:.2f}")
            print(f"R²   : {metrics['R2']:.4f}")

            input("\nPresione una tecla para volver al menú principal.")


        elif option == "3":

            while True:
                dashboard_option = get_dashboard_option()
                if dashboard_option == "5":
                    break

                visualizer.open_chart(dashboard_option)

        elif option == "4":
            predictor.predict_laptop()

        elif option == "5":
            break

        else:
            print("\nOpción inválida.")


if __name__ == "__main__":

    try:
        main()
    
    except KeyboardInterrupt:
        print("\nAplicación cancelada por el usuario.")