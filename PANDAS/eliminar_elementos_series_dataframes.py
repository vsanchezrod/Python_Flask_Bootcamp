import pandas as pd
import numpy as np

# ELIMINAR ELEMENTOS EN UNA SERIE
print('ELIMINAR ELEMENTOS EN UNA SERIE')

# Devuelve un array de 3 elementos de 0 al 4-1
print(np.arange(4))
print('\n')

# CREAR SERIE
serie = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
print(serie)
print('\n')

# ELIMINAR ELEMENTO CON EL INDEX => DROP(indice a borrar)
serie = serie.drop('c')
print(serie)
print('\n')

# ELIMINAR ELEMENTOS EN UN DATAFRAME
print('ELIMINAR ELEMENTOS EN UN DATAFRAME')

# Se va a crear un dataframe con 3 filas por 3 columnas (reshape), por ello se necesitan 9 valores
print(np.arange(9).reshape(3, 3))
print('\n')

lista_valores = np.arange(9).reshape(3, 3)
lista_indices = ['a', 'b', 'c']
lista_columnas = ['c1', 'c2', 'c3']

# CREAR DATAFRAME
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
print('\n')

# ELIMINAR FILA CON EL INDEX => DROP(indice a borrar)
dataframe = dataframe.drop('b')
print(dataframe)
print('\n')

# ELIMINAR COLUMNA CON EL NOMBRE DE LA COLUMNA => DROP(nombreColumna, axis=1 Es el eje de las columnas)
dataframe = dataframe.drop('c2', axis=1)
print(dataframe)
print('\n')