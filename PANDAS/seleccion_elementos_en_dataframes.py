import pandas as pd
import numpy as np

# CREAR DATAFRAME
lista_valores = np.arange(25).reshape(5,5)
print(lista_valores)
print('\n')

lista_indices = ['i1', 'i2', 'i3', 'i4', 'i5']
lista_columnas = ['c1', 'c2', 'c3', 'c4', 'c5']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
print('\n')

# ACCEDER A UNA COLUMNA [nombreColumna]
print(dataframe['c2'])
print('\n')

# ACCEDER A UN VALOR DE UNA COLUMNA [nombreColumna][nombreÍndice]
print(dataframe['c2']['i2'])
print('\n')

# SELECCIONAR VARIAS COLUMNAS POR NOMBRE
print(dataframe[['c3', 'c4']])
print('\n')

# SELECCIONAR RANGO DE COLUMNAS
print(dataframe.loc[:, 'c2':'c5'])
print('\n')

# SELECCIONAR POR VALOR
# Ejemplo: en la columna 2 aquellos valores mayores que 15
print(dataframe[dataframe['c2'] > 15])
print('\n')

# SABER SI SE CUMPLE UNA CONDICIÓN
# Ejemplo: elementos del dataframe mayores de 20
print(dataframe > 20)
print('\n')

# BÚSQUEDA POR ÍNDICE => LOC [nombreÍndice o númeroÍndice]
print(dataframe.loc['i3'])
print('\n')

# SELECCIONAR ELEMENTO CON FILA Y COLUMNA => LOC [nombreÍndice][nombreColumna]
print(dataframe.loc['i3']['c4'])
print('\n')


# PARA SELECCIONAR POR FILA => USAR MÉTODO LOC
# PARA SELECCIONAR POR COLUMNA => NO HACE FALTA EL MÉTODO LOC a menos que sea para seleccionar rangos de columnas