import pandas as pd
import numpy as np

# CREAR LISTA DE VALORES con 10 filas por 3 columnas
lista_valores = np.random.rand(10, 3)
print(lista_valores)
print('\n')

# CREAR DATAFRAME
dataframe = pd.DataFrame(lista_valores)
print(dataframe)
print('\n')

# SELECCIONAR PRIMERA COLUMNA DEL DF
print("SELECCIONAR PRIMERA COLUMNA")
columna = dataframe[0]
print(columna)
print('\n')

# SELECCIONAR VALORES DENTRO DE LA PRIMERA COLUMNA
print("SELECCIONAR VALORES DENTRO DE LA PRIMERA COLUMNA MAYORES DE 0.4")
datos_mayores_40_columna = columna[columna > 0.40]
print(datos_mayores_40_columna)
print('\n')

# SELECCIONAR VALORES DENTRO DEL DATAFRAME
print("SELECCIONAR VALORES DENTRO DEL DATAFRAME MAYORES DE 0.4")
datos_mayores_40_dataframe = dataframe[dataframe > 0.40]
print(datos_mayores_40_dataframe)
print('\n')
