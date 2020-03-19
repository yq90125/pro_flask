#encoding:utf-8
from flask import Flask
from App.views import init_view
from App.models import init_model
def create_app():
    app = Flask(__name__)
    #uri 数据库+驱动(py中有的数据库比如sqlite不需要写驱动)://用户名:密码@主机:端口/数据库名
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_model(app)
    init_view(app)
    return app
