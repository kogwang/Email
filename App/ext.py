from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
# from flask_session import Session

from App.models import db

migrate = Migrate()



def init_app(app):
    migrate.init_app(app=app,db=db)
    Bootstrap(app=app)