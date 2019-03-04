import pandas as pd

print("REEMPLAZAR DAOTS EN SERIES")

# CREAR SERIE
serie = pd.Series([1, 2, 3, 4, 5], index=list('abcde'))
print(serie)
print('\n')

# REEMPLAZAR UN VALOR POR OTRO => REPLACE()
serie2 = serie.replace(1, 6)
print(serie2)
print('\n')

# CON DICCIONAR => En lugar de poner valores se le puede pasar un diccionario
serie3 = serie.replace({2: 8, 3: 9})
print(serie3)
print('\n')
