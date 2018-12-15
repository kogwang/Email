from flask_migrate import Migrate

from App.models import db

migrate = Migrate()

def init_app(app):
    migrate.init_app(app=app,db=db)