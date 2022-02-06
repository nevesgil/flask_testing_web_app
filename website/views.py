# anything not related to authentication may go in this file
# logins goes on the auth file

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# whatever goes on home will run the bellow function
@views.route('/')
def home():
    return render_template("home.html")
