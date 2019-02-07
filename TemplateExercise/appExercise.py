from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    num_end = False

    username = request.args.get("username")

    # Si hay una letra que sea minuscula dentro de username => True
    lower_letter = any(letra.islower() for letra in username)

    # Si hay una letra que sea mayuscula dentro de username => True
    upper_letter = any(letra.isupper() for letra in username)

    # Si el último caracter es un número => True
    num_end = username[-1].isdigit()

    # Variable que recoge si se cumplen o no todas las condiciones
    report = lower_letter and upper_letter and num_end

    return render_template("report.html", report=report, lower_letter=lower_letter, upper_letter=upper_letter,
                           num_end=num_end)


if __name__ == "__main__":
    app.run(debug=True)
