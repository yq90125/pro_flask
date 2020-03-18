from flask import Blueprint,render_template
blue = Blueprint('first_blue', __name__)
@blue.route('/')
def index():
    #return 'I am first blueprint Index'
    return render_template('index.html',msg='sleep')
@blue.route('/f_2')
def f2():
    return 'I am first blueprint page 2'