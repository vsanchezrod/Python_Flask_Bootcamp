from flask import Flask
# Para montar un API RESTFUL con FLASH
from flask_restful import Resource, Api

app = Flask(__name__)
# API (recibe la app)
api = Api(app)

puppies = []


class PuppyNames(Resource):

    # RECUPERAR UNA MASCOTA
    def get(self, name):

        # Buscar una mascota por nombre recorriendo el diccionario
        for puppy in puppies:
            # Se accede al valor de la clave name y se compara con el nombre que entra
            if puppy['name'] == name:
                return puppy

        # Si no se encuentra la mascota, se devuelve un objeto vacío.
        # Se le puede pasar el tipo de error que es
        return {"name": None}, 404

    # GUARDAR UNA MASCOTA
    def post(self, name):
        # Recibe un nombre y crea un objeto puppy
        puppy = {"name": name}

        # Agrega el objeto al diccionarop de puppies
        puppies.append(puppy)

        # Devuelve la mascota
        return puppy

    # BORRAR UNA MASCOTA
    def delete(self, name):

        # Se recorre las mascotas obteniendo la mascota y su index dentro del diccionario
        for index, puppy in enumerate(puppies):

            # Si se encuentra la mascota buscando por el nombre, se borrará con el método pop al que se le pasa el index
            if puppy["name"] == name:
                deleted_pup = puppies.pop(index)
                return {"note": "delete success"}

        # Si no lo encuentra
        return {"note": "No se ha encontrado la mascota a borrar"}, 404


class AllNames(Resource):

    def get(self):
        # Va a devolver todas las mascotas
        return {"puppies": puppies}


# Se crea una clase que hereda de Resource
class HelloWorld(Resource):

    # Método get
    def get(self):
        # Devuelve un JSON
        return {"Hello": "Hello world"}


# Antes de lanzar la APP, es necesario conectar las clases (RESOURCES) con una URL

# Se definen los endpoints con los parámetros que vana recibir
api.add_resource(PuppyNames, "/puppy/<string:name>")
api.add_resource(AllNames, "/puppies")
api.add_resource(HelloWorld, "/")

if __name__ == '__main__':
    app.run(debug=True)
