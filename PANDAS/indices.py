import pandas as pd

# ÍNDICES EN SERIES
print('SERIES e ÍNDICES')

# CREAR SERIE A PARTIR DE UNA LISTA
lista_valores = [1, 2, 3]
lista_indices = ['a', 'b', 'c']

serie = pd.Series(lista_valores, index=lista_indices)
print(serie)
print('\n')

# Devuelve los VALORES DE LOS ÍNDICES EN FORMA DE LISTA. Los índices de las series no soportan cambios
print(serie.index)
print('\n')

# Se puede obtener el primer índice
print(serie.index[0])
print('\n')

# ÍNDICES EN DATAFRAMES
print('DATAFRAMES e ÍNDICES')
lista_valores2 = [[6, 7, 8], [8, 9, 5], [6, 9, 7]]
lista_indices2 = ['matemáticas', 'historia', 'fisica']
lista_nombres = ['Antonio', 'María', 'Pedro']

# Se crea el dataframe con los valores, la lista que determinará los índices, y la lista que determinará las columnas
dataframe = pd.DataFrame(lista_valores2, index=lista_indices2, columns=lista_nombres)
print(dataframe)
print('\n')

# VER ÍNDICES DE UN DATAFRAME
print(dataframe.index)
print('\n')

# ACCEDER a un ÍNDICE
print(dataframe.index[0])
print('\n')