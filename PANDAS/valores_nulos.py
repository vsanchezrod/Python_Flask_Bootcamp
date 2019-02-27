import pandas as pd
import numpy as np

# SERIES
# Con np.nan se crea un valor nulo.

lista_valores = ['1', '2', np.nan, '4']
serie = pd.Series(lista_valores, index=list('abcd'))
print(serie)
print('\n')

# MËTODO QUE DEVUELVE SI LOS VALORES SON NULOS => isnull()
print(serie.isnull())
print('\n')

# MËTODO QUE BORRAR LOS VALORES NULOS (todas las filas que tengan algun valor nulo) => dropna()
print(serie.dropna())
serie = serie.dropna()
print(serie)
print('\n')

# DATAFRAMES
lista_valores = [[1, 2, 3], [4, np.nan, 5], [6, 7, np.nan]]
lista_indices = list('123')
lista_columnas = list('adc')
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
print('\n')

# MËTODO QUE DEVUELVE SI LOS VALORES SON NULOS => isnull()
print(dataframe.isnull())
print('\n')

# MËTODO QUE BORRAR LOS VALORES NULOS (todas las filas que tengan algun valor nulo) => dropna()
print(dataframe.dropna())
print('\n')

# MËTODO QUE RELLENA LOS NULOS CON UN VALOR => fillna(x)
print(dataframe.fillna(0))
print('\n')