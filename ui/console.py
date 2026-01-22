# ui/console.py
import pandas as pd


def solicitar_ruta_archivo():
    ruta = input("Introduce la ruta del archivo CSV: ").strip()
    return ruta

def solicitar_columna_objetivo(nombre_predeterminado="target"):
    columna = input(f"Introduce el nombre de la columna objetivo (por defecto: '{nombre_predeterminado}'): ").strip()
    return columna if columna else nombre_predeterminado

def mostrar_resumen_general(dimensiones):
    print("\n=== RESUMEN GENERAL ===")
    print(f"Número de instancias (filas): {dimensiones['filas']}")
    print(f"Número de atributos (columnas): {dimensiones['columnas']}")

def mostrar_estadisticas_numericas(stats_numericas):
    print("\n=== ESTADÍSTICAS NUMÉRICAS ===")
    if not stats_numericas:
        print("No se encontraron columnas numéricas.")
        return
    for col, stats in stats_numericas.items():
        print(f"\nColumna: {col}")
        print(f"  Mínimo: {stats['min']}")
        print(f"  Máximo: {stats['max']}")
        std_val = stats['std']
    if std_val is not None and str(std_val).lower() != 'nan':
        print(f"  Desviación estándar: {std_val:.4f}")
    else:
        print("  Desviación estándar: N/A")
        print(f"  Valores no nulos: {stats['no_nulos']}")

def mostrar_balance_clases(balance_clases):
    print("\n=== BALANCE DE CLASES ===")
    if balance_clases is None:
        print("No se pudo analizar el balance de clases (columna objetivo no encontrada).")
        return
    print("Conteos por clase:")
    for clase, conteo in balance_clases["conteos"].items():
        proporcion = balance_clases["proporciones"][clase]
        print(f"  {clase}: {conteo} ({proporcion:.2%})")

def mostrar_error(mensaje):
    print(f"\n❌ ERROR: {mensaje}")