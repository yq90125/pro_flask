from flask_script import Manager
from App import create_app
app = create_app()
manager = Manager(app=app)
if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=8000)
    manager.run()
