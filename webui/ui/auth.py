from flask import Blueprint, request, flash, redirect, url_for
from flask.templating import render_template
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        flash("Wrong Email or Password!", category='error')
    
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>logout</p>"


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', 'error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', 'error')
        elif password1 != password2:
            flash('Passwords don\'t match.', 'error')
        elif len(password1) < 6:
            flash('Password must be at least 6 characters.', 'error')
        else:
            if len(User.query.all()) == 0:
                role = "Admin"
            else:
                role = "User"
            new_user = User(email=email,
                            password=generate_password_hash(password1,
                                                            method='pbkdf2:'
                                                            'sha256:100',
                                                            salt_length=16),
                            name=name, role=role)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', 'success')
            return redirect(url_for('views.home'))

    return render_template("register.html")
