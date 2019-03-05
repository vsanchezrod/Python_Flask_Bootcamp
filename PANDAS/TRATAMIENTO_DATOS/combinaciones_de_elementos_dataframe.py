import pandas as pd
import numpy as np

# CREAR LISTA DE VALORES
lista_valores = np.arange(25).reshape(5, 5)
print(lista_valores)
print('\n')

# CREAR DATAFRAME
dataframe = pd.DataFrame(lista_valores)
print(dataframe)
print('\n')

# CREAR COMBINACION ALEATORIA => np.random.permutation(n)
print("CREAR COMBINACION ALEATORIA")
'''
    np.random.permutation(n)
    Genera un array aleatorio desde n hasta n-1
'''

combinacion_aleatoria = np.random.permutation(5)
print(combinacion_aleatoria)
print('\n')

# DESORDENAR EL DATAFRAME A PARTIR DE LA COMBINACION ALEATORIA => df.take(combinacion_aleatoria)
print("DESORDENAR DATAFRAME A PARTIR DE LA COMBINACION ALEATORIA")
'''
    dataframe.take(combinacion)
    Organiza las filas del dataframe en función de la combinación aleatoria
'''

dataframe2 = dataframe.take(combinacion_aleatoria)
print(dataframe2)
print('\n')
