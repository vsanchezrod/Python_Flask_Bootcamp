import pandas as pd

# CREAR LISTA DE PRECIOS
precios = [42, 55, 48, 23, 5, 21, 88, 34, 26]
rango_precios = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# AGRUPAR PRECIOS => pd.cut
'''
    Cada uno de los precios los va a ir agrupando dentro del rango correspondiente.
    El resultado de usar el método cut, nos va a indicar uno a uno los rangos en los que está incluído cada uno
    de los precios, es decir, por cada precio nos indicará en que categoría de precios está.
'''

print("AGRUPAR PRECIOS POR RANGOS")
precios_agrupados_por_rango = pd.cut(precios, rango_precios)
print(precios_agrupados_por_rango)
print('\n')


# CONTAR VALORES AGRUPADOS => pd.value.counts

print("CONTAR VALORES PRESENTES EN CADA RANGO")
contador_rangos_precios = pd.value_counts(precios_agrupados_por_rango)
print(contador_rangos_precios)
print('\n')

