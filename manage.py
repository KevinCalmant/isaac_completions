"""
manage.py
    - provides a command line utility for interacting with the app 
      (Debugging and setup)
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from isaapp.application import create_app
from isaapp.models import db


app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db)


if __name__ == '__main__':
    manager.run()
