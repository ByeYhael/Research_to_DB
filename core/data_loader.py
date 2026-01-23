# data_loader.py
import pandas as pd

def cargar_dataset(ruta_archivo):
    if not pd.io.common.file_exists(ruta_archivo):
        raise FileNotFoundError("El archivo no fue encontrado")
    
    try:
        # Aquí -999.0 es NaN
        dataset = pd.read_csv(
            ruta_archivo,
            na_values=[-999.0, -888.0, "-999.0", "-888"],  # maneja varios formatos
            keep_default_na=True
        )
    except Exception as e:
        raise ValueError(f"Error al leer el CSV: {e}")

    if dataset.empty:
        raise ValueError("El archivo está vacío")

    return dataset