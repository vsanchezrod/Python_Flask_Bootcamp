# Fecha y hora

# Importar módulo para las fechas
from datetime import datetime

# FECHA Y HORA ACTUAL => datetime.now()
print("FECHA Y HORA")
fecha_hora = datetime.now()
print(fecha_hora)
print('\n')


# ACCEDER A LAS DISTINTAS PARTES DE LA FECHA
print("ACCEDER A LAS DISTINTAS PARTES DE LA FECHA")

# FECHA
year = fecha_hora.year
print(year)

mes = fecha_hora.month
print(mes)

dia = fecha_hora.day
print(dia)
print('\n')


# HORA
hora = fecha_hora.hour
print(hora)

minutos = fecha_hora.minute
print(minutos)

segundos = fecha_hora.second
print(segundos)

milisegundos = fecha_hora.microsecond
print(milisegundos)
print('\n')

print(f"LA HORA ES: {hora}:{minutos}:{segundos}")
print('\n')