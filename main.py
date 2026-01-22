# main.py

from ui import console
from core import data_loader, analyzer

def main():
    # 1. Obtener entrada del usuario
    ruta_archivo = console.solicitar_ruta_archivo()
    
    try:
        # 2. Cargar datos
        dataset = data_loader.cargar_dataset(ruta_archivo)
        
        # 3. Solicitar configuración adicional (variable objetivo)
        columna_target = console.solicitar_columna_objetivo("target")
        
        # 4. Realizar análisis (Lógica de Negocio)
        dimensiones = analyzer.obtener_dimensiones(dataset)
        stats_numericas = analyzer.analizar_columnas_numericas(dataset)
        balance_clases = analyzer.analizar_balance_clases(dataset, columna_target)
        
        # 5. Mostrar resultados (UI)
        console.mostrar_resumen_general(dimensiones)
        console.mostrar_estadisticas_numericas(stats_numericas)
        console.mostrar_balance_clases(balance_clases)
        
    except Exception as e:
        console.mostrar_error(str(e))

if __name__ == "__main__":
    main()