from flask import Blueprint, render_template, request

views = Blueprint("views_blueprint", __name__, static_folder="static", template_folder="templates")


@views.route("/home")
@views.route("/")
def render_home():
    return render_template("home.html")


@views.route('/kontakt/')
def contact():
    return render_template("contact.html")


@views.route('/about/')
def about():
    return render_template("about.html")


@views.route('/wiedza')
def carbon_footprint_article():
    section = request.args.get('section')
    if section == 'slad-weglowy':
        return render_template('carbon-footprint-article.html', section='slad-weglowy')
    elif section == 'po-co-liczyc-slad-weglowy':
        return render_template('carbon-footprint-article.html', section='po-co-liczyc-slad-weglowy')
    elif section == 'jak-liczyc-slad-weglowy':
        return render_template('carbon-footprint-article.html', section='jak-liczyc-slad-weglowy')
    else:
        return render_template('carbon-footprint-article.html')  # Default render


@views.route('/kalkulator-emisji/')
def emission_calculator():
    return render_template("emission-calculator.html")