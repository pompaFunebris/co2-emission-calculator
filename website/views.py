import csv

from flask import Blueprint, render_template, request, jsonify

views = Blueprint("views_blueprint", __name__, static_folder="static", template_folder="templates")


@views.route("/home")
@views.route("/")
def render_home():
    return render_template("about.html")


@views.route('/kontakt/')
def contact():
    return render_template("contact.html")


@views.route('/about/')
def about():
    return render_template("about.html")


@views.route('/kalkulator-emisji/', methods=['GET', 'POST'])
def emission_calculator():
    if request.method == 'POST':
        material_names = request.form.getlist('material_name[]')
        material_volumes = request.form.getlist('material_volume[]')

        insulator_names = request.form.getlist('insulator_name[]')
        insulator_volumes = request.form.getlist('insulator_volume[]')

        finishing_names = request.form.getlist('finishing_name[]')
        finishing_volumes = request.form.getlist('finishing_volume[]')

        other_names = request.form.getlist('other_name[]')
        other_quantities = request.form.getlist('other_volume[]')

        print(f"Mat names: {material_names}")
        print(f"Mat volumes: {material_volumes}")

        print(f"insulator_names: {insulator_names}")
        print(f"insulator_volumes: {insulator_volumes}")

        print(f"finishing_names: {finishing_names}")
        print(f"finishing_volumes: {finishing_volumes}")

        print(f"other_names: {other_names}")
        print(f"other_quantities: {other_quantities}")

        return 'Data received successfully!'
    else:
        return render_template('emission-calculator.html')


@views.route('/material-options')
def get_material_options():
    material_options = {
        "material": [],
        "insulation": [],
        "finishing": [],
        "other": []
    }

    # Read material options from CSV file
    files = ['main-materials.csv', 'insulators.csv', 'finishing-materials.csv', 'other-materials.csv']
    categories = ['material', 'insulation', 'finishing','other']

    i = 0
    for file in files:
        with open(f'website/static/materials/{file}', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                label = row['Material']
                value = row['Value']
                # category = row['Category']
                unit = row['Unit']
                material_options[categories[i]].append({
                    'label': label,
                    'value': value,
                    'unit': unit
                })
        i = i+1

    print(material_options["insulation"])
    return jsonify(material_options)


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
