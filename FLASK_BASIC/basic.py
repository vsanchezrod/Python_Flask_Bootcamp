from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def index():
    return "<h1>Hello puppy!!</h1>"


@app.route('/information')  # 127.0.0.1:5000/information
def info():
    return "<h1>Puppies are cute!!</h1>"


# Ruta dinámica que recibe una variable
@app.route('/puppy/<name>')  # 127.0.0.1:5000/puppy/VARIABLE
def puppy(name):
    return "Puppy name: {}".format(name)


@app.route('/puppy_latin/<name>')  # 127.0.0.1:5000/puppy_latin/VARIABLE
def puppylatin(name):
    pupname = ""
    if name[-1] == "y":
        pupname = name[:-1] + "iful"
    else:
        pupname = name + "y"

    return "<h1>Your puppy latin name is: {}</h1>".format(pupname)


if __name__ == "__main__":
    app.run(debug=True)
