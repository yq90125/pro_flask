from flask import Blueprint
second_blue = Blueprint('second_blue', __name__)
@second_blue.route('/second_blue')
def index():
    return 'I am second blueprint Index'
@second_blue.route('/s2')
def s2():
    return 'I am second blueprint page 2'
