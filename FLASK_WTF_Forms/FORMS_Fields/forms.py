from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
#  Diferentes tipos de campos
from wtforms import (StringField, BooleanField, RadioField,
                     SelectField, TextAreaField, SubmitField)

# Validaciones de los formularios
from wtforms.validators import DataRequired

app = Flask(__name__)

# Configuración de la aplicación
app.config['SECRET_KEY'] = 'mykey'


# Se crea una clase que crea formularios (hereda de la clase FlaskForm)
class InfoForm(FlaskForm):
    # A los campos se le pasa las validaciones en forma de lista y se instancian
    breed = StringField("What Breed are you?", validators=[DataRequired()])
    neutered = BooleanField("have you benn neutered?")

    # A los radiobuttons se les pasa las opciones a traves de "choices (label, value)
    mood = RadioField("Please choose your mood:",
                      choices=[("mood_one", "Happy"), ("mood_two", "Sad")])

    food_choice = SelectField("Pick your favorite food:",
                              choices=[("chi", "chicken"), ("bf", "beef"), ("fish", "fish")])

    feedback = TextAreaField()
    submit = SubmitField("Submit")


# A través de los methods se permite mandar el formulario al template
@app.route('/', methods=["GET", "POST"])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        # Si la validación es correcta cogelos los datos y redirigimos a otra página
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        # Si la validación es correcta, se redirige a otra URL
        return redirect(url_for('thankyou'))

    return render_template("index.html", form=form)


# A través de los methods se permite mandar el formulario al template
@app.route('/thankyou', methods=["GET", "POST"])
def thankyou():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)
