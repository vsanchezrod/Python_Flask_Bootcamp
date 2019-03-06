'''
    try... except... else... finally
'''

# numero1 = 5
# numero2 = 0
# division = numero1 / numero2
# print(division)  # MUESTRA ERROR DE DIVISION ENTRE 0

print('EXCEPCIONES GENERALES')
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except:
    print('Ha habido un error')

print('\n')

# ZeroDivisionError
print('EXCEPCIONES ESPECÏFICAS')
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except:
    print('Ha habido un error')

print('\n')

print('AÑADIMOS UN ELSE PARA SI NO SE PRODUCE EXCEPCIÓN CONFIGURAR INSTRUCCIONES')
try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except:
    print('Ha habido un error')
else:
    print('La división funcionó correctamente')

print('\n')


print('FINALLY -> Permite ejecutar un código independientemente de que se haya fallado o no ')
try:
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except:
    print('Ha habido un error')
else:
    print('La división funcionó correctamente')
finally:
    print('División terminada')

print('\n')


print('FINALLY -> Permite ejecutar un código independientemente de que se haya fallado o no ')
try:
    numero1 = 5
    numero2 = 2
    division = numero1 / numero2
    print(division)
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except:
    print('Ha habido un error')
else:
    print('La división funcionó correctamente')
finally:
    print('División terminada')

print('\n')