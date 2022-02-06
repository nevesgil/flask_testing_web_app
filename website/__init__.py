from flask import Flask


def create_app():
    app = Flask(__name__)
    # try linking the secret on the key vault
    app.config['SECRET_KEY'] = 'senhakaren'
    # those need to be here
    from .views import views
    from .auth import auth
    # those need to be registered
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app
