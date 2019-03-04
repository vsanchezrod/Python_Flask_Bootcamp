import pandas as pd

print("ELIMINAR DUPLICADOS EN DATAFRAMES")
# CREAR DATAFRAME

lista_valores = [[1, 2], [1, 2], [5, 6], [5, 8]]
lista_indices = list('mnop')
lista_columnas = ['valor1', 'valor2']

dataframe1 = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe1)
print('\n')

# La fila con indice M y N tiene los mismos valores
# Para eliminar las filas que contengan elementos duplicados ==> df.drop_duplicates()

# ELIMINAR DUPLICADOS EN FILAS
print("DUPLICADOS EN FILAS")
dataframe2 = dataframe1.drop_duplicates()
print(dataframe2)
print('\n')


# ELIMINAR DUPLICADOS EN COLUMNAS
print("DUPLICADOS EN COLUMNAS")
dataframe3 = dataframe1.drop_duplicates(['valor1'])
print(dataframe3)
print('\n')

# Se queda con el primero, si queremos mantener el último se añade KEEP='last'

dataframe4 = dataframe1.drop_duplicates(['valor1'], keep='last')
print(dataframe4)
print('\n')