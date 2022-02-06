# anything not related to authentication may go in this file
# logins goes on the auth file

from flask import Blueprint

views = Blueprint('views', __name__)

# whatever goes on home will run the bellow function
@views.route('/')
def home():
    return "<h1>Test</h1>"