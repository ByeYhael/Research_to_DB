# ui/visualizer.py
import matplotlib.pyplot as plt

def graficar_histogramas_pobreza_por_sexo(dataset):
    """
    Genera 8 histogramas (uno por variable de pobreza),
    comparando hombres (azul) y mujeres (rosa).
    """
    variables = [
        'pobreza_porcentaje',
        'carencia_rezago_educativo_porcentaje',
        'carencia_servicios_de_salud_porcentaje',
        'carencia_seguridad_social_porcentaje',
        'carencia_calidad_espacios_vivienda_porcentaje',
        'carencia_servicios_basicos_vivienda_porcentaje',
        'carencia_alimentacion_nutritiva_calidad_porcentaje',
        'ingreso_inferior_a_lpi_porcentaje'
    ]

    # Filtrar datos por sexo
    df_hombres = dataset[dataset['sexo'] == 'hombres']
    df_mujeres = dataset[dataset['sexo'] == 'mujeres']

    # Crear subgráficas (2 filas x 4 columnas)
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()

    for i, var in enumerate(variables):
        if var not in dataset.columns:
            continue

        ax = axes[i]
        # Histograma para hombres
        ax.hist(df_hombres[var], bins=30, alpha=0.6, color='blue', label='Hombres')
        # Histograma para mujeres
        ax.hist(df_mujeres[var], bins=30, alpha=0.6, color='pink', label='Mujeres')

        ax.set_title(var.replace('_', ' ').title(), fontsize=12)
        ax.set_xlabel('Porcentaje (%)')
        ax.set_ylabel('Frecuencia (número de localidades)')
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)

    # Ajustar layout
    plt.tight_layout()
    plt.suptitle('Distribución de Indicadores de Pobreza por Sexo\n(Base: pobreza_grupos_poblacionales_sexo.csv)', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.show()