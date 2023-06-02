#Routes for the Website
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def landingpage():
    return render_template("landingpage.html")

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/app')
def app():
    return render_template("app.html")
