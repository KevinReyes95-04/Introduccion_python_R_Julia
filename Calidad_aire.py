#--------------------------------------
# Calidad del Aire en Bogotá (DataFrames y Filtrado)
#--------------------------------------

# Importacion de librerias
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Creacion de dataframe de calidad de aire 

df_aire = pd.DataFrame({
    "Estacion": ["Carvajal", "Kennedy", "Fontibón", "Suba", "Usaquén"],
    "PM25": [55, 42, 38, 15, 12],
    "PM10": [20, 40, 30, 50, 35],
    "NO2": [15, 30, 20, 40, 25]
})
print("DataFrame de Calidad del Aire:")
print(df_aire)


# Resumen tecnico del datframe 
print("\nResumen técnico del DataFrame:")
print(df_aire.info())

# Estadísticas descriptivas del dataframe
print("\nEstadísticas descriptivas del DataFrame:")
print(df_aire.describe())

# Filtrado de alertas mayores a 15
df_alerta = df_aire [(df_aire["PM25"] > 15)]
print("\nEstaciones con PM2.5 mayor a 15:")
print(df_alerta[["Estacion", "PM25"]])

# Asignacion de valor critico de PM2.5
df_aire["Alerta_PM25"] = np.where(df_aire["PM25"] > 15, "Crítico", "Normal")
print("\nDataFrame con Alerta de PM2.5:")
print(df_aire[["Estacion", "PM25", "Alerta_PM25"]])

# Creacion de grafico de barras para PM2.5
plt.figure(figsize=(10, 5))
plt.bar(df_aire["Estacion"], df_aire["PM25"], color="blue")
plt.xlabel("Estación")
plt.ylabel("PM2.5 (μg/m³)")
plt.title("Calidad del Aire - PM2.5 por Estación")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

