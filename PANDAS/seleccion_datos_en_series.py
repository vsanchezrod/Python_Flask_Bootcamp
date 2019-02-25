import pandas as pd
import numpy as np

# CREAR SERIE A TRAVÉS DE UNA LISTA
lista_valores = np.arange(3)
lista_indices = ['i1', 'i2', 'i3']
print(lista_valores)
print('\n')

serie = pd.Series(lista_valores, index=lista_indices)
print(serie)
print('\n')

# OPERACIONES SOBRE SERIES
serie = serie * 2
print(serie)
print('\n')

# ACCEDER A UN ELEMENTO EN UNA SERIE a través del nombre del índice
print(serie['i2'])
print('\n')

# ACCEDER A UN ELEMENTO EN UNA SERIE a través del número del índice
print(serie[1])
print('\n')

# ACCEDER UNOS ELEMENTOS POSICIONADOS ENTRE DOS ÍNDICES (0 incluído, 2 no incluído) Posición inicial - P.final -1
print(serie[0:2])
print('\n')

# ACCEDER UNOS ELEMENTOS POSICIONADOS ENTRE DOS NOMBRES DE ÍNDICES (0 incluído, 2 no incluído) Posición inicial - P.final
print(serie['i1':'i3'])
print('\n')

# SELECCIONAR A TRAVÉS DE UNA CONDICIÓN
print(serie[serie > 3])
print(serie)
print('\n')

# CAMBIAR EL VALOR
serie[serie > 3] = 6
print(serie)
print('\n')