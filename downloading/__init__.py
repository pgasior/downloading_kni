from flask import Flask
from flask_bootstrap import Bootstrap

UPLOAD_FOLDER = 'c:/flask_uploads/'

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


import downloading.views

if __name__ == '__main__':
    app.run()
