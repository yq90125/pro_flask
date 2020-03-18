from .first_blue import blue
from .second_blue import second_blue
from flask import render_template
def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second_blue)