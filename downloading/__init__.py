from flask import Flask

UPLOAD_FOLDER = 'c:/flask_uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import downloading.views

if __name__ == '__main__':
    app.run()
