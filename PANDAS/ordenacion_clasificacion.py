import pandas as pd
import numpy as np

# CREAR SERIE
lista_valores = range(4)
lista_indices = list('CABD')
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)
print('\n')

# ORDENAR POR ÍNDICE => sort_index()
print(serie.sort_index())
print('\n')

# ORDENAR POR VALORES => sort_values()
print(serie.sort_values())
print('\n')

# CREAR RANKING A PARTIR DE UNA SERIE Y SUS VALORES => rank() Rabking de menor a mayor
print(serie.rank())
print('\n')


# CREAR SERIE MÁS GRANDE
serie2 = pd.Series(np.random.randn(10))
print(serie2)
print(serie2.rank())