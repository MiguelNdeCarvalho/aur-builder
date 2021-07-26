from flask import Flask
from flask_toastr import Toastr

toastr = Toastr()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwgjhehnwgnwjgwjgpqwdqw'

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    toastr.init_app(app)

    return app
