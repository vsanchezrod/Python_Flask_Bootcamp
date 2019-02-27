import pandas as pd
import numpy as np

# CREAR DATAFRAME
array = np.array([[1, 8, 3], [5, 6, 7]])
dataframe = pd.DataFrame(array, index=['a', 'b'], columns=list('123'))
print(dataframe)
print('\n')

# FUNCIONES

# - SUMA
print('SUMA => Suma por columnas (toda la columna)')
print(dataframe.sum())
print('\n')

print('SUMA => Suma por filas (toda la fila)')
print(dataframe.sum(axis=1))
print('\n')


# - MÍNIMO VALOR
print('VALOR MÍNIMO por columna')
print(dataframe.min())
print('\n')

print('VALOR MÍNIMO por fila')
print(dataframe.min(axis=1))
print('\n')

# - ÍNDICE DEL MÍNIMO VALOR
print('ÍNDICE DEL VALOR MÍNIMO por columna')
print(dataframe.idxmin())
print('\n')

print('ÍNDICE DEL VALOR MÍNIMO por fila')
print(dataframe.idxmin(axis=1))
print('\n')


# - MÁXIMO VALOR
print('VALOR MÁXIMO por columna')
print(dataframe.max())
print('\n')

print('VALOR MÁXIMO por fila')
print(dataframe.max(axis=1))
print('\n')

# - ÍNDICE DEL MÁXIMO VALOR
print('ÍNDICE DEL VALOR MÁXIMO por columna')
print(dataframe.idxmax())
print('\n')


print('ÍNDICE DEL VALOR MÁXIMO por fila')
print(dataframe.idxmax(axis=1))
print('\n')


# - VALORES ESTADÍSTICOS DE UN DATAFRAME
print('Número de elementos, medio, min, max, percentiles, ...')
print(dataframe.describe())
print('\n')