from flask import Blueprint,render_template
from App.models import db
blue = Blueprint('first_blue', __name__)
@blue.route('/')
def index():
    return render_template('index.html',msg='sleep')
@blue.route('/f_2')
def f2():
    return 'I am first blueprint page 2'
@blue.route('/createdb')
def createdb():
    db.create_all()
    #db.drop_all()
    return 'success'