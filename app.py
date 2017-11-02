from flask import Flask, jsonify, render_template
from livereload import Server

import requests

from random import randint

from config import APP_KEY, APP_SECRET

app = Flask('MemeFeed')
app.debug = True

def fb_request(endpoint):
    return 'https://graph.facebook.com/v2.10/{}?access_token={}|{}'.format(endpoint, APP_KEY, APP_SECRET) 

@app.route('/')
def root():
    resp = requests.get(fb_request('1717731545171536/feed/'))
    data = resp.json()['data']
    random_post =  data[randint(0,len(data))]
    print(len(data))
    message = random_post['message'] if 'message' in random_post else '[No text]'
    post_attachment = requests.get(fb_request(random_post['id']  + '/attachments/')).json()['data'][0]

    if 'media' in post_attachment and 'image' in post_attachment['media'] and 'src' in post_attachment['media']['image']:
        src = post_attachment['media']['image']['src']
    else:
        src = ''
        
    return render_template('meme.html', text=message, imgsrc=src)

@app.route('/<post>')
def post(post):
    resp = requests.get(fb_request(str(post)  + '/attachments')).json()
    return render_template('meme.html', text='Hello', imgsrc='')

Server(app.wsgi_app).serve()


