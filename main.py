# main.py
from ui import console
from ui.visualizer import graficar_histogramas_pobreza_por_sexo
from core import data_loader, analyzer
import pandas as pd

def main():
    ruta_archivo = console.solicitar_ruta_archivo()
    
    try:
        # Cargar y preprocesar datos
        dataset = data_loader.cargar_dataset(ruta_archivo)
        
        # Extraer sexo y participación (ajusta índices si es necesario)
        if dataset.shape[1] > 4:
            dataset['sexo'] = dataset.iloc[:, 4].astype(str).str.split(": ").str[1]
        else:
            raise ValueError("Columna de sexo no encontrada.")
            
        if dataset.shape[1] > 7:
            dataset['participacion'] = pd.to_numeric(dataset.iloc[:, 7], errors='coerce')
        else:
            raise ValueError("Columna de participación no encontrada.")
            
        dataset = dataset.dropna(subset=['sexo', 'participacion'])

        # Análisis
        dimensiones = analyzer.obtener_dimensiones(dataset)
        stats_numericas = analyzer.analizar_columnas_numericas(dataset)
        balance_clases = analyzer.analizar_balance_clases(dataset, 'sexo')
        
        # Mostrar resultados
        console.mostrar_resumen_general(dimensiones)
        console.mostrar_estadisticas_numericas(stats_numericas)
        console.mostrar_balance_clases(balance_clases)
        
        # 📊 Graficar
        graficar_histogramas_pobreza_por_sexo(dataset)   
             
    except Exception as e:
        console.mostrar_error(str(e))

if __name__ == "__main__":
    main()