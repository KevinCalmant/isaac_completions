"""
manage.py
    - Provides a cli utility for the app (Debugging && setup)
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from isaapi.application import create_app
from isaapi.models import db, User

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# Provides migration utility commands
manager.add_command('db', MigrateCommand)


# Enable the python shell with app context 
@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                User=User)


if __name__ == '__main__':
    manager.run()
