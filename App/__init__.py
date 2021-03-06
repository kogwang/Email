
from flask import Flask

from App.models import init_sql
from App.views import blue
from App.setting import env
from App.ext import init_app


def create_app():
    app=Flask(__name__)
    app.register_blueprint(blueprint=blue)
    app.config.from_object(env.get('develop'))
    init_app(app)
    init_sql(app)
    return app