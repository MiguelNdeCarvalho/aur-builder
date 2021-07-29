from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    active = db.Column(db.Boolean(), nullable=False, default=False)

    def is_admin(self):
        return self.admin

    def is_active(self):
        return self.active
