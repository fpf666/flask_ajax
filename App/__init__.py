from flask import Flask

from App.ext import init_app
from App.models import init_sql
from App.setting import env
from App.urls import init_api


def creater_app(con):
    app = Flask(__name__)
    app.config.from_object(env.get(con))
    init_api(app)
    init_app(app)
    init_sql(app)
    return app