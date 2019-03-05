import pandas as pd
import numpy as np

# CREAR LISTA DE VALORES
lista_valores = {'clave1': ['x', 'x', 'y', 'y', 'z'], 'clave2': ['a', 'b', 'a', ' b', 'a'],
                 'datos1': np.random.rand(5), 'datos2': np.random.rand(5)}
print(lista_valores)
print('\n')

# CREAR DATAFRAME
dataframe = pd.DataFrame(lista_valores)
print(dataframe)
print('\n')

# AGRUPAR DATOS DE LA COLUMNA DATOS1 en función de la COLUMNA CLAVE1 => groupby
print("AGRUPAR DATOS DE LA COLUMNA DATOS1 en función de la COLUMNA CLAVE1")
'''
    La columna "datos1" se va a agrupar en función de los valores de la columna "clave1"
    Se crea una serie agrupada
'''

grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])
print(grupo1)
print('\n')

print("VER VALORES DENTRO DE LA AGRUPACIÓN")
'''
    La columna "datos1" se va a agrupar en función de los valores de la columna "clave1"
    Se crea una serie agrupada
'''
print("MEDIA")
print(grupo1.mean())
print('\n')

print("MAX")
print(grupo1.max())
print('\n')

print("MIN")
print(grupo1.min())
print('\n')
