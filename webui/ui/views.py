from flask import Blueprint, render_template
from flask_login import login_required, current_user
from libgravatar import Gravatar
from .models import User

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    if current_user.is_active():
        if current_user.is_admin():
            return render_template('index.html', user=current_user,
                                    packages=2,
                                    registeredUsers=len(User.query
                                                        .filter_by(active=True)
                                                        .all()),
                                    pendingUsers=len(User.query
                                                    .filter_by(active=False)
                                                    .all()),
                                    pendingRequests=5,
                                    gravatar=getGravatar(current_user, 160))
        else:
            return render_template('index.html', user=current_user,
                                    gravatar=getGravatar(current_user, 160))
    else:
        return "oi"


def getGravatar(user, size):
    g = Gravatar(user.email)
    return g.get_image(size=size)
