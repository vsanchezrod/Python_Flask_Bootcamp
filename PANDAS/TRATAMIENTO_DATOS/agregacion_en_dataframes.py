import pandas as pd
import numpy as np

# CREAR LISTA DE VALORES
lista_valores = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], [np.nan, np.nan, np.nan]]
print(lista_valores)
print('\n')

lista_columnas = list('abc')

# CREAR DATAFRAME
dataframe = pd.DataFrame(lista_valores, columns=lista_columnas)
print(dataframe)
print('\n')


# DEPRECADO EN VERSION PANDAS 0.24
print("NO VA BIEN - no se si está deprecado")

# AGREGACIÓN - AGRUPAR PARA OBTENER UN VALOR => agg()
print("AGREGACIÓN - AGRUPAR PARA OBTENER UN VALOR")
'''
    Se va a hacer una agrupación, para obtener la suma y el mínimo valor
'''

# dataframe_agrupacion = dataframe.agg(['sum', 'min'])
# print(dataframe_agrupacion)
# print('\n')


# DEPRECADO EN VERSION PANDAS 0.24
dataframe_agrupacion = dataframe.agg('sum', axis=1)
print(dataframe_agrupacion)
print('\n')
