from flask import Blueprint, render_template
from flask_login import login_required, current_user
from libgravatar import Gravatar
from .models import User

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    if current_user.role == "Admin":
        return render_template('index.html', user=current_user,
                               users=User.query.all(),
                               gravatar=getGravatar(current_user, 160))
    else:
        return render_template('index.html', user=current_user,
                               gravatar=getGravatar(current_user, 160))


def getGravatar(user, size):
    g = Gravatar(user.email)
    return g.get_image(size=size)
