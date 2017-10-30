from flask import Flask, jsonify, render_template
from livereload import Server

import requests

from config import APP_KEY, APP_SECRET

app = Flask('MemeFeed')
app.debug = True

 

@app.route('/')
def root():
    resp = requests.get('https://graph.facebook.com/v2.10/1717731545171536/feed/?access_token={}|{}'.format(APP_KEY, APP_SECRET))
    print(resp.json())
    # return (jsonify(resp.json()), resp.status_code, resp.headers.items())
    return render_template('meme.html', text="hey", imgsrc="http://flask.pocoo.org/docs/0.12/_static/flask.png")

Server(app.wsgi_app).serve()