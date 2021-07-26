from flask import Flask
from flask_toastr import Toastr
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

toastr = Toastr()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwgjhehnwgnwjgwjgpqwdqw'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    toastr.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    # flake8: noqa: F401
    from .models import User

    create_database(app)

    return app


def create_database(app):
    if not path.exists("ui/" + DB_NAME):
        db.create_all(app=app)
