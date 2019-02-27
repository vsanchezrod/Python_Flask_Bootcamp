import pandas as pd

# CREAR 1 DATAFRAME
print('DATAFRAME 1')
dataframe1 = pd.DataFrame({'c1': ['1', '2', '3'], 'clave': ['a', 'b', 'c']})
print(dataframe1)
print('\n')


# CREAR 2 DATAFRAME
print('DATAFRAME 2')
dataframe2 = pd.DataFrame({'c2': ['4', '5', '6'], 'clave': ['c', 'b', 'e']})
print(dataframe2)
print('\n')


# UNIÓN DE LOS DOS DATAFRAMES ES UN NUEVO DATAFRAME ==> MERGE(df1,df2)

# UNIÓN DE LA PARTE COMÚN
'''
    En los dos dataframes existe una columna que coincide que es clave, aunque tienen distintos valores.
    Va a buscar las claves en común y va a unir los valores
    Las claves que no tengan en común van a desaparecer
'''

print('Aparecen todos los datos comunes de los dos dataframe')
dataframe3 = pd.DataFrame.merge(dataframe1, dataframe2)
print(dataframe3)
print('\n')

# SE PUEDE UNIR POR LA COLUMNA QUE SE QUIERA UTILIZANDO EL ATRIBUTO ON=nombreColumna
dataframe3 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave')




# UNIÓN DE LA PARTE COMÚN + LEFT O RIGHT

'''
    Ejemplo:
        - Prevalece el dataframe 1 y le va a añadir las partes comunes del dataframe2
        Con how left o right se establece cual es el dataframe que predomina
'''

print('LEFT => Prevalece el dataframe de la izquierda')
dataframe4 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='left')
print(dataframe4)
print('\n')


print('RIGHT => Prevalece el dataframe de la derecha')
dataframe5 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='right')
print(dataframe5)
print('\n')


print('OUTER => Aparecen todos los datos de los dos dataframes, no solo los comunes')
dataframe6 = pd.DataFrame.merge(dataframe1, dataframe2, on='clave', how='outer')
print(dataframe6)
print('\n')