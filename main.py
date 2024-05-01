from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, redirect, url_for, render_template
# from home import home as home_blueprint
#
# app = Flask(__name__)  # Flask constructor
# app.register_blueprint(home_blueprint)
#
#
# @app.route('/')
# def hello():
#     return render_template("home.html")
#
#
# @app.route('/kontakt/')
# def contact():
#     return render_template("contact.html")
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

