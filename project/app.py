from flask import Flask, render_template, request, jsonify
from qasis.qasis_main import *
import requests

app = Flask(__name__)

def get_config():
    CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    KEY = 'da927f0ca807c7723e82bf817fde43d2'

    url = CONFIG_PATTERN.format(key=KEY)
    r = requests.get(url)
    config = r.json()
    print config['images']
    return config

def get_poster(id,config):
    KEY = 'da927f0ca807c7723e82bf817fde43d2'
    base_url = config['images']['base_url']

    IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}' 
    r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=id))
    api_response = r.json()

    max_size = 'w342'
    posters = api_response['posters']
    poster_urls = []
    for poster in posters:
        rel_path = poster['file_path']
        url = "{0}{1}{2}".format(base_url, max_size, rel_path)
        poster_urls.append(url)
    return poster_urls


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qasis')
def qasis():
    query = request.args.get('query')
    results = qasis_main(query,'','')
    config = get_config()
    results = [{"id": x, "data": y['object'], "score":y['score'],"poster":get_poster(x,config)} for (x,y) in results]
    return jsonify({"results": results})

@app.route('/hello')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True, port = 5000)


