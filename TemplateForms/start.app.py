from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/thank')
def thank():
    # Recoger los datos que llegan al HTML desde el formulario con request.arg.get('name')
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thank.html', first=first, last=last)


# Para manejar rutas erróneas
@app.errorhandler(404)
# Se le pasa por convención una e para error
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
