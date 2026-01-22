import pandas as pd

def obtener_dimensiones(dataset):
    return {
        "filas": dataset.shape[0],
        "columnas": dataset.shape[1]
    }

def analizar_columnas_numericas(dataset):
    df_numeric = dataset.select_dtypes(include='number')
    resultados = {}
    for nombre_columna in df_numeric.columns:
        serie = df_numeric[nombre_columna]
        resultados[nombre_columna] = {
            "min": serie.min(),
            "max": serie.max(),
            "std": serie.std(),
            "no_nulos": serie.count()
        }
    return resultados

def analizar_balance_clases(dataset, nombre_columna_target):
    if nombre_columna_target not in dataset.columns:
        return None
    columna = dataset[nombre_columna_target]
    total_instancias = len(dataset)
    conteos = columna.value_counts()
    proporciones = columna.value_counts(normalize=True)
    return {
        "conteos": conteos.to_dict(),
        "proporciones": proporciones.to_dict()
    }