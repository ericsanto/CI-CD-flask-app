from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello. Iam FLask"


@app.route("/testea")
def teste():
    return "Essa é uma página de teste"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

