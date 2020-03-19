#encoding:utf-8
from .first_blue import blue
from .second_blue import second_blue
def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second_blue)