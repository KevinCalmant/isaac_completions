"""
manage.py
    - provides a command line utility for interacting with the app 
      (Debugging and setup)
"""
import os
from flask import jsonify
from flask_script import Manager, Shell, Command, Server
from flask_migrate import Migrate, MigrateCommand
from flask_security import Security, auth_token_required
from flask_security.datastore import SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
from sqlalchemy.exc import IntegrityError

from api import create_app, db
from api.models import User, Role 


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


def make_shell_context():
    return dict(app=app, db=db)


class DBInit(Command):
    ''' Init and create tables from models '''
    def __init__(self, db):
        self.db = db

    def run(self):
        self.db.create_all()


class DBRegUser(Command):
    ''' Create base user in the DB '''
    def __init__(self, db):
        self.db = db

    def run(self):
        for i in range(2):
            try:
                user_datastore.create_user(
                    email='test{}@test.com'.format(i),
                    password=encrypt_password('test'),
                    first_name='John{}'.format(i),
                    last_name='Doe{}'.format(i)
                )
                self.db.session.commit()
            except IntegrityError:
                pass


@app.route('/')
def index():
    return "Hello world !"


@app.route('/dummy-api/', methods=['GET'])
@auth_token_required
def dummyAPI():
    rec_dict = {
        "Key1": "Value1",
        "Key2": "Value2"
    }
    return jsonify(items=rec_dict)


manager.add_command('runserver', Server(host="localhost", port=5000))
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('bd_create_reg_user', DBRegUser(db))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
