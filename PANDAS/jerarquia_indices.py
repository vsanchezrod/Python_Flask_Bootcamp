import pandas as pd
import numpy as np

print('---------CREAR UNA SERIE CON DOBLE ÍNDICE Y GENERAR UN DATAFRAME A PARTIR DE ESTE ==> SERIE.UNSTACK()---------')
# Se crea una lista de números aleatorios
lista_valores = np.random.rand(6)
print(lista_valores)
print('\n')

# Se crea una lista de índices que en este caso será doble porque habrá varios índices
'''
    [ [Índice de primer nivel], [Índice de segundo nivel]  ]
'''
lista_indices = [[1, 1, 1, 2, 2, 2], ['a', 'b', 'c', 'a', 'b', 'c']]
print(lista_indices)
print('\n')

# CREAR SERIE
serie = pd.Series(lista_valores, index=lista_indices)
print('SERIE CON DOBLE ÍNDICE')
print(serie)
print('\n')

# ACCEDER A LOS VALORES A TRAVÉS DE LOS ÍNDICES
'''
    serie[Índice de primer nivel][Índice de segundo nivel]
'''
print(serie[1]['b'])
print('\n')

# CREAR UN DATAFRAME a través de una serie con doble índice
print('DATAFRAME CREADO A PARTIR DE LA SERIE CON DOBLE INDICE')
dataframe = serie.unstack()
print(dataframe)
print('\n')


print('---------CREAR UNA SERIE CON DOBLE ÍNDICE A PARTIR DE UN DATAFRAME ==> DATAFRAME.STACK()------------')

# CREAR UN DATAFRAME
lista_valores2 = np.arange(16).reshape(4, 4)
lista_indices2 = list('1234')
lista_columns2 = list('abcd')
dataframe2 = pd.DataFrame(lista_valores2, index=lista_indices2, columns=lista_columns2)
print(dataframe2)
print('\n')

# CREAR SERIE
serie2 = dataframe2.stack()
print(serie2)
print('\n')