from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def index():
    # render_template - Busca en el directorio templates el html que cargará
    # Se le pueden pasar variables (lista, diccionarios, ...)

    nombre = "Vir"
    letras = list(nombre)
    diccionario = {"Nombre": "Bango"}
    listaMascotas = {"Rufus", "Bango", "Lolo"}

    usuarioLogado = True;

    return render_template('index.html', nombre=nombre, letras=letras, diccionario=diccionario,
                           listaMascotas=listaMascotas, usuarioLogado=usuarioLogado)


if __name__ == "__main__":
    app.run(debug=True)
