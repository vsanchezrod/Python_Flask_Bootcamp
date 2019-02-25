import pandas as pd

# CREAR UNA SERIE => Es una lista de valores pero indexada
serie1 = pd.Series([3, 5, 7])
print('\n')
print(serie1)

# Para ACCEDER a un ELEMENTO
print('\n')
print(serie1[1])

# CREAR DOS LISTAS: asignaturas y notas
asignatures = ['matemáticas', 'historia', 'fisica', 'literatura']
notas_daniel = [8, 6, 9, 7]
notas_ana = [7, 8, 5, 9]

# CREAR SERIES BASÁNDOSE EN DATOS DE LISTAS, donde el index sea la lista de asignaturas
serie_notas_daniel = pd.Series(notas_daniel, index=asignatures)
print('\n')
print(serie_notas_daniel)

serie_notas_ana = pd.Series(notas_ana, index=asignatures)
print('\n')
print(serie_notas_ana)


# Para ACCEDER a un INDEX a la nota de física
print('\n')
print(serie_notas_daniel['fisica'])

# Para ACCEDER A DATOS a partir de una CONDICIÓN a la notas mayores o iguales a 8 (Nos da el index y la nota)
print('\n')
print(serie_notas_daniel[serie_notas_daniel >= 8])

# Poner NOMBRE a la SERIE
print('\n')
serie_notas_daniel.name = "Notas de Daniel"
print(serie_notas_daniel)

# Poner NOMBRE a los ÍNDICES de la serie
print('\n')
serie_notas_daniel.index.name = "Asignaturas de Daniel"
print(serie_notas_daniel)

# Devuelve los VALORES DE LOS ÍNDICES EN FORMA DE LISTA. Los índices de las series no soportan cambios
print(serie_notas_daniel.index)
print('\n')

# Se puede obtener el primer índice
print(serie_notas_daniel.index[0])
print('\n')

# CONVERTIR SERIE A DICCIONARIO (pierde los nombres de la serie y de los índices)
print('\n')
diccionario = serie_notas_daniel.to_dict()
print(diccionario)

# CONVERTIR DICCIONARIO A SERIE
print('\n')
serie = pd.Series(diccionario)
print(serie)

# SE PUEDEN HACER OPERACIONES SOBRE LAS SERIES
# CREAR SERIE CON DATOS DE VARIAS SERIES (nota media de los alumnos de la clase)
print('\n')
serie_notas_clase = (serie_notas_daniel + serie_notas_daniel) / 2
print(serie_notas_clase)
