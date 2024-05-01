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


@views.route('/kalkulator-emisji/', methods=['GET', 'POST'])
def emission_calculator():
    if request.method == 'POST':
        # Retrieve form data
        materials_volume = float(request.form['materials_volume'])
        insulation_volume = float(request.form['insulation_volume'])
        finishings_volume = float(request.form['finishings_volume'])
        other_quantity = int(request.form['other_quantity'])

        # Calculate CO2 emission (replace with actual calculation)
        total_co2_emission = 0.0
        total_co2_emission += materials_volume * 10  # Example emission calculation for materials
        total_co2_emission += insulation_volume * 10  # Example emission calculation for insulation
        total_co2_emission += finishings_volume * 10  # Example emission calculation for finishings
        total_co2_emission += other_quantity * 0.1  # Example emission calculation for other

        return render_template('co2_calculator_result.html', total_co2_emission=total_co2_emission)
    else:
        return render_template('emission-calculator.html')

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


# @views.route('/kalkulator-emisji/')
# def emission_calculator():
#     return render_template("emission-calculator.html")
