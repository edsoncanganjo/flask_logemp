from flask import Flask
from maisqfood.ext import site
from maisqfood.ext import config
from maisqfood.ext import toolbar
from maisqfood.ext import db
from maisqfood.ext import cli

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app