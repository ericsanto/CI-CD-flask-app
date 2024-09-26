from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello. Iam FLask"


@app.route("/testeabc")
def teste():
    return "Essa. e uma pagina para teste"

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

