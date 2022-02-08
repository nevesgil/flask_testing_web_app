# anything not related to authentication may go in this file
# logins goes on the auth file
from flask_login import login_required, current_user
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

# whatever goes on home will run the bellow function
@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)
