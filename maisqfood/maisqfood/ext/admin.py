from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from maisqfood.ext.db import db
from maisqfood.ext.db.models import Category

admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "MaisQfooD")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap2")
    admin.init_app(app)

    # Proteger com código de acesso
    # Traduzir para mais idiomas

    admin.add_view(ModelView(Category, db.session))