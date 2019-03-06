# GENERACIÓN DE DOCUMENTACIÓN - cadenas para documentación

# COMENTARIOS PARA FUNCIONES

def saludar(nombre):
    """
    Comentario comentando el objetivo de la función
    :param nombre:
    """
    print("Buenos días " + nombre)


saludar("Vir")

# Nos ofrece la documentación de la función => help(funcion).
help(saludar)


# COMENTARIO PARA CLASES
class Saludo:
    """
    Esta clase tendrá dos funciones: buenos_dias y adios
    Ambas funciones recibirán como parámetro un nombre
    """

    def buenos_dias(self, nombre):
        """
        Función que da los buenos días a una persona
        :param nombre:
        """
        print(f"Buenos días {nombre}")


    def adios(self, nombre):
        """
        Función que despide una persona
        :param nombre:
        """
        print(f"Hasta luego {nombre}")


saludo = Saludo()

saludo.buenos_dias("Virginia")
saludo.adios("Virginia")

help(Saludo)