from flask import Flask
from website.views import views


def create_app():
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views)

    return app


