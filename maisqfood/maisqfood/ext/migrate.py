from flask_migrate import Migrate
from maisqfood.ext.db import db
from maisqfood.ext.db import models #noqa

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)

