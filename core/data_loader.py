# data_loader.py
import pandas as pd
import os

def cargar_dataset(ruta_archivo):
    """
    Carga un archivo CSV en un DataFrame.
    """
    # Verificar si el archivo existe
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError("El archivo no fue encontrado")

    # Cargar usando pandas
    try:
        dataset = pd.read_csv(ruta_archivo)
    except Exception as e:
        raise ValueError(f"Error al leer el CSV: {e}")

    # Verificar si el dataset está vacío
    if dataset.empty:
        raise ValueError("El archivo está vacío")

    return dataset