from flask import Flask, render_template, request, jsonify
from qasis.qasis_main import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qasis')
def qasis():
    query = request.args.get('query')
    results = qasis_main(query,'','')
    results = [{"name": x, "score": y} for (x,y) in results]
    return jsonify({"results": results})

@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
