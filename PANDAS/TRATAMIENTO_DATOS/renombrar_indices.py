import pandas as pd
import numpy as np

# CREAR DATAFRAME
lista_valores = np.arange(9).reshape(3, 3)
lista_indices = list('abc')

dataframe = pd.DataFrame(lista_valores, index=lista_indices)
print(dataframe)
print('\n')

# CAMBIAR INDICES A MAYUSCULAS => df.index.map(str.upper)
print("CAMBIAR A MAYUS")
nuevos_indices = dataframe.index.map(str.upper)
dataframe.index = nuevos_indices
print(dataframe)
print('\n')

# RENAME INDICES A MINUSCULAS=> df.rename(index=str.lower)
print("RENOMBRAR A MINUS")
dataframe = dataframe.rename(index=str.lower)
print(dataframe)
print('\n')

# RENAME INDICES A OTRAS NOMBRES=> df.rename(index=str.lower)
print("RENOMBRAR A OTROS STRINGS")

# Crear un diccionario para renombrar
nuevos_indices = {'a': 'f', 'b': 'g', 'c': 'h'}
dataframe2 = dataframe.rename(index=nuevos_indices)
print(dataframe)
print('\n')


# INPLACE => Para guardar los cambios dentro de la variable sin tener que igual el dataframe

dataframe.rename(index=nuevos_indices, inplace=True)
print(dataframe)
print('\n')