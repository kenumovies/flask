from flask import Flask, render_template
from sassutils.wsgi import SassMiddleware


app = Flask(__name__)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'project': ('static/sass', 'static/css', '/static/css')
})




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)
