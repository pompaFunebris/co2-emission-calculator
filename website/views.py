from flask import Blueprint, render_template

views = Blueprint("home", __name__, static_folder="static", template_folder="templates")


@views.route("/home")
@views.route("/")
def render_home():
    return render_template("home.html")


@views.route('/kontakt/')
def contact():
    return render_template("contact.html")