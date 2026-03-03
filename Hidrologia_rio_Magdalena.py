#--------------------------------------
# Ejercicio 1: Hidrología del Río Magdalena (Vectores y Matemáticas)
#--------------------------------------

# Importacion de librerias
import numpy as np
import pandas as pd 

# Definición de variables 
Estaciones = [ "Honda", "Puerto Berrío", "Barrancabermeja", "Puerto Wilches", "Calamar"]
Caudalesm3s = [1500, 2100, 2800, 3200, 4500]
print("Estaciones:", Estaciones)
print("Caudales (m3/s):", Caudalesm3s)

# Calculo promedio y media
promedio_caudal = sum(Caudalesm3s) / len(Caudalesm3s)
print("Promedio de caudal (m3/s):", promedio_caudal)

# Calculo del caudal máximo y mínimo
caudal_maximo = max(Caudalesm3s)
caudal_minimo = min(Caudalesm3s)
print("Caudal máximo (m3/s):", caudal_maximo)
print("Caudal mínimo (m3/s):", caudal_minimo)

# Caudales en litros por segundo usando vectorizacion
caudales_lps = np.array(Caudalesm3s) * 1000
print("Caudales (L/s):", caudales_lps)

# Listros pos segundo con separacion de miles
caudales_lps_formateados = np.array([f"{caudal:,.0f}" for caudal in caudales_lps])
print("Caudales (L/s) formateados:", caudales_lps_formateados)

# Porcentaje de caudal respecto al total con 2 decimales
porcentaje_caudal = (np.array(Caudalesm3s) / sum(Caudalesm3s)) * 100
print("Porcentaje de caudal respecto al total (%):", np.round(porcentaje_caudal, 2))

