from flask import Blueprint, render_template
from flask_login import login_required, current_user
from libgravatar import Gravatar

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('index.html', user=current_user,
                           gravatar=getGravatar(current_user, 160))


def getGravatar(user, size):
    g = Gravatar(user.email)
    return g.get_image(size=size)
