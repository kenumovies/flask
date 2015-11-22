from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello kittens!"
@app.route("/fuck")
def yo():
    return "Fuck!"
@app.route('/hello/', methods=['POST'])
def function():
    payload =  request.data
    return payload


if __name__ == "__main__":
    app.run()
