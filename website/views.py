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
        total_emission = 0
        chosen_materials = []

        # Define the categories and corresponding CSV files
        categories = ['material', 'insulator', 'finishing', 'other']
        kategorie = ['Materiał główny', 'Termoizolacje', 'Wykończenia', 'Pozostałe']
        files = ['main-materials.csv', 'insulators.csv', 'finishing-materials.csv', 'other-materials.csv']

        for category, file, kategoria in zip(categories, files, kategorie):
            names = request.form.getlist(f'{category}_name[]')
            volumes = request.form.getlist(f'{category}_volume[]')
            material_data = []

            with open(f'website/static/materials/{file}', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    label = row['Material']
                    value = row['Value']
                    unit = row['Unit']

                    if label in names:
                        index = names.index(label)
                        volume = volumes[index]
                        total_emission += float(volume) * float(value)
                        material_data.append({'name': label, 'volume': volume, 'unit': unit})

            chosen_materials.append({'category': kategoria, 'data': material_data})

        # Convert total emission to metric tons
        total_emission = round(total_emission / 1000, 2)

        return render_template('emission-calculator.html', total_emission=total_emission, chosen_materials=chosen_materials)
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
