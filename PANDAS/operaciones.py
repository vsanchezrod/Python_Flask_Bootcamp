import pandas as pd
import numpy as np

# CREAR SERIES
serie1 = pd.Series([0, 1, 2], index=['a', 'b', 'c'])
print(serie1)
print('\n')

serie2 = pd.Series([3, 4, 5, 6], index=['a', 'b', 'c', 'd'])
print(serie2)
print('\n')

# OPERACIONES

# SUMA DE SERIES - Se suman las columnas que tiene el mismo índice
print(serie1 + serie2)
print('\n')
# Como la serie1 no tiene índice 'd', el valor de la suma es NaN



# CREAR DATAFRAMES
lista_valores = np.arange(4).reshape(2, 2)
print(lista_valores)
print('\n')

# LIST() => CONSTRUYE UNA LISTA con los elementos, serapándolos
lista_indices = list('ab')
print(lista_indices)
print('\n')

lista_columnas = list('12')
print(lista_columnas)
print('\n')

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
print('\n')

lista_valores2 = np.arange(9).reshape(3, 3)
lista_indices2 = list('abc')
lista_columnas2= list('123')

dataframe2 = pd.DataFrame(lista_valores2, index=lista_indices2, columns=lista_columnas2)
print(dataframe2)
print('\n')

# OPERACIONES
# SUMA DE DATAFRAMES - Se suman los elementos que coinciden en fila y columna y los que no se ponen a NaN
dataframe3 = dataframe + dataframe2
print(dataframe3)
print('\n')

# Seleccionamos ahora del dataframe3 los elementos que existen
dataframe3[dataframe3 >= 0]
print(dataframe3)
print('\n')

# Al dataframe 1 se le pueden añadir los valores del dataframe 2 que no tenga, rellenado con valores = 0 y sumando los del dataframe2
dataframe.add(dataframe2, fill_value=0)
print(dataframe.add(dataframe2, fill_value=0))
print('\n')