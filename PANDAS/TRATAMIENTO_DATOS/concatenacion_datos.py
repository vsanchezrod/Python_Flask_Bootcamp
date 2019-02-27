import pandas as pd
import numpy as np

print('CONCETENACIÓN DE ARRAYS, SERIES Y DATAFRAMES')
print('\n')

print('CONCETENACIÓN DE ARRAYS')
# CREAR UN ARRAY
array = np.arange(9).reshape(3, 3)
print(array)
print('\n')

# CONCATENAR ARRAYS => concatenate([array1, array2])
print('ARRAY CONCATENADO hacia abajo')
print(np.concatenate([array, array]))
print('\n')

print('ARRAY CONCATENADO hacia la derecha')
print(np.concatenate([array, array], axis=1))
print('\n')

print('CONCETENACIÓN DE SERIES')
serie1 = pd.Series([1, 2, 3], index=list('abc'))
serie2 = pd.Series([4, 5, 6], index=list('def'))
print(serie1)
print('\n')
print(serie2)
print('\n')

# CONCATENAR SERIES => concat([serie1, serie2])
print('SERIES CONCATENADAS')
print(pd.concat([serie1, serie2]))
print('\n')

# print('ARRAY CONCATENADO añandiendo una CLAVE') => NO ME FUNCIONA
# print(pd.concat([serie1, serie2]), keys=['serie1', 'serie2'])
# print('\n')

print('CONCETENACIÓN DE DATAFRAMES')
dataframe1 = pd.DataFrame(np.random.rand(3, 3), columns=['a', 'b', 'c'])
dataframe2 = pd.DataFrame(np.random.rand(2, 3), columns=['a', 'b', 'c'])
print(dataframe1)
print('\n')
print(dataframe2)
print('\n')

# CONCATENAR DATAFRAMES => concat([dataframe1, dataframe2])
print('DATAFRAMES CONCATENADOS')
dataframe3 = pd.concat([dataframe1, dataframe2])
print(dataframe3)
print('\n')

print('DATAFRAMES CONCATENADOS IGNORANDO LOS ÍNDICES')
dataframe4 = pd.concat([dataframe1, dataframe2], ignore_index=True)
print(dataframe4)
print('\n')