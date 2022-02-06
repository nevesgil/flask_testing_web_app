from flask import Flask


def create_app():
    app = Flask(__name__)
    # try linking the secret on the key vault
    app.config['SECRET_KEY'] = 'senhakaren'

    return app
