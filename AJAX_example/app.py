from flask import Flask, render_template, request
from flask.json import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        a = request.json['data']
        # a = request.args.get('a', 0, type=int)
        print(a)
        b = request.args.get('b', 0, type=int)
        print(b)

        return jsonify(result=a + b)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
