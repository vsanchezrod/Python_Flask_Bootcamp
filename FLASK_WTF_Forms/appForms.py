from flask import Flask, render_template
# Formularios con Flask
from flask_wtf import FlaskForm
# Tipos de campos de los formularios con Flask
from wtforms import StringField, SubmitField

app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = 'mysecretkey'


# Se crea una clase que crea formularios (hereda de la clase FlaskForm)
class InfoForm(FlaskForm):
    breed = StringField("What Breed are you?")  # Lo que está escrito es el LABEL
    submit = SubmitField("Submit")


# A través de los methods se permite mandar el formulario al template
@app.route('/', methods=["GET", "POST"])
def index():
    breed = False

    # Se crea una instancia del formulario
    form = InfoForm()

    # Cuando se produce el evento on submit si la validación es OK
    if form.validate_on_submit():
        # Se asigna a la variable breed el valor del input del form
        breed = form.breed.data

        # Después se resetea el valor del formulario
        form.breed.data = ""

    return render_template("index.html", form=form, breed=breed)


if __name__ == "__main__":
    app.run(debug=True)
