import pandas as pd

# Módulo para sacar datos de una web
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
# webbrowser.open(website) # Abre en un navegador la ruta

# Se crea una DATAFRAME a veces que los datos copiados en el portapapeles
# dataframe_nba = pd.read_clipboard()
dataframe_nba = pd.read_csv('nba.csv')
print(dataframe_nba)
print('\n')

# VER COLUMNAS - .columns, devuelve la lista con los nombres de las columnas
print(dataframe_nba.columns)
print('\n')

# VER DATOS DE UNA COLUMNA
print(dataframe_nba['Campeón del Oeste'])
print('\n')

# VER DATOS POR ÍNDICE (Ver fila) => LOC[indice]
print(dataframe_nba.loc[5])
print('\n')

# VER PRIMEROS ELEMENTOS del dataframe => HEAD() Muestra las 5 primeras
print(dataframe_nba.head())
print('\n')

# VER X PRIMEROS ELEMENTOS del dataframe => HEAD(X) Muestra las X primeros
print(dataframe_nba.head(3))
print('\n')

# VER ÚLTIMOS ELEMENTOS del dataframe => TAIL() Muestra los 5 últimos
print(dataframe_nba.tail())
print('\n')

# VER X ÚLTIMOS ELEMENTOS del dataframe => TAIL(X) Muestra los X último
print(dataframe_nba.tail(3))
print('\n')


# CREAR DATAFRAME A PARTIR DE UN DICCIONARIO {Clave: valor}
lista_asignaturas = ['matemáticas', 'historia', 'fisica']
lista_notas = [7, 8, 9]

diccionario = {'Asignaturas': lista_asignaturas, 'Notas': lista_notas}
print(diccionario)
print('\n')

datafram_notas = pd.DataFrame(diccionario)
print(datafram_notas)
print('\n')