from flask_migrate import Migrate, MigrateCommand

from app import app
from flask_script import Manager

from app.models import db

manage = Manager(app)
migrate = Migrate(app, db)
manage.add_command('db', MigrateCommand)

@manage.command
def create():
    db.create_all()
    return  'created'

if __name__ == '__main__':
    from werkzeug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()