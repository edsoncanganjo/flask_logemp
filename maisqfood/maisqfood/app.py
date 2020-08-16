from flask import Flask
from maisqfood.ext import site
from maisqfood.ext import config
from maisqfood.ext import toolbar
from maisqfood.ext import db
from maisqfood.ext import migrate
from maisqfood.ext import cli
from maisqfood.ext import hooks
from maisqfood.ext import auth
from maisqfood.ext import admin

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    hooks.init_app(app)
    return app