
from datetime import datetime
from flask_socketio import SocketIO

from flask_sqlalchemy import SQLAlchemy
import requests, os

from bs4 import BeautifulSoup as bs

from vicks.encrypt import encryptpdf as enc
from flask import Flask, flash, url_for, session, request, redirect, render_template, send_from_directory

from PIL import Image
import ast, json, urllib.request as ur

UPLOAD_FOLDER = 'uploads'
try:
    os.mkdir('uploads')
except Exception as e:
    print(e)
    pass

app = Flask(__name__)
app.secret_key = "secret key"

socketio = SocketIO(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def ytc():
    from vicks import ytc

    vid = 'LjXbmAmXxfY'
    dict = ytc.comments(vid)

    return render_template("ytc.html",
                            dict=dict,
                            vid=vid)

@app.route('/converted_ytc', methods=['POST'])
def converted_ytc():
    from vicks import ytc

    url = request.form['ytc']
    s = url.split('/')

    if s[2] == 'www.youtube.com':
        vid = s[3].split('=')[1].split('?')[0]
    elif s[2] == 'youtu.be':
        vid = s[3].split('?')[0]
    else:
        print("Sorry... Code couldn't be extracted !!!")

    dict = ytc.comments(vid)

    return render_template("ytc.html",
                            dict=dict,
                            vid=vid)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    socketio.run(app, debug=True)
