# Es posible capturar diferentes excepciones, poniéndolas de forma consecutiva
def divide():
    try:
        op1 = float(input("Introduzca primer número"))
        op2 = float(input("Introduzca segundo número"))

        print("La división es: " + str(op1 / op2))



    except ValueError:
        print("El valor introducido es erróneo")


    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    # Cuando se quiere ejecutar una sentencia SIEMPRE se usa finally, tanto si ocurre una expceción como si no
    finally:

        # Esto es muy común para cerrar la conexión con la base de datos
        print("Cálculo finalizado")


divide()


# Es posible capturar diferentes excepciones de forma general (menos recomendable)
def divide2():
    try:
        op1 = float(input("Introduzca primer número"))
        op2 = float(input("Introduzca segundo número"))

        print("La división es: " + str(op1 / op2))


    except:
        print("Ha ocurrido un error")

    print("Cálculo finalizado")


divide2()


# Es posible usar solo try finally, no se captura el error, pero es obligatorio usar el finally
def divide3():
    try:
        op1 = float(input("Introduzca primer número"))
        op2 = float(input("Introduzca segundo número"))

        print("La división es: " + str(op1 / op2))


    finally:
        print("Cálculo finalizado")


divide3()

