from flask import Flask
from flask.helpers import url_for


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwgjhehnwgnwjgwjgpqwdqw'

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app
