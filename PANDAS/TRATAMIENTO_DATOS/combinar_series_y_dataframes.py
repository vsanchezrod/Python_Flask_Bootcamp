import pandas as pd
import numpy as np

print("COMBINAR SERIES")
# COMBINAR SERIES => serie1.combine_first(serie2)

serie1 = pd.Series([1, 2, np.nan])
print(serie1)
print('\n')

serie2 = pd.Series([4, 5, 6])
print(serie2)
print('\n')

# Si encuentra un valor NULO, lo cambia por el valor que tenga la serie2
print("SERIE 3")
serie3 = serie1.combine_first(serie2)
print(serie3)
print('\n')


print("COMBINAR DATAFRAMES")
# COMBINAR DATAFRAMES => dataframe1.combine_first(datafram2)

lista_valores1 = [1, 2, np.nan]
dataframe1 = pd.DataFrame(lista_valores1)
print(dataframe1)
print('\n')

lista_valores2 = [4, 5, 6]
dataframe2 = pd.DataFrame([4, 5, 6])
print(dataframe2)
print('\n')

# Si encuentra un valor NULO, lo cambia por el valor que tenga el dataframe2
print("DATAFRAME 3")
dataframe3 = dataframe1.combine_first(dataframe2)
print(serie3)
print('\n')
