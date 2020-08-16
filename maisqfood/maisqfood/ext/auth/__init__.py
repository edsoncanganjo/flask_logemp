from maisqfood.ext.auth import models #noqa
from maisqfood.ext.auth.commands import list_users, add_user

from maisqfood.ext.db import db
from maisqfood.ext.auth.admin import UserAdmin
from maisqfood.ext.admin import admin
from maisqfood.ext.auth.models import User

def init_app(app):
    """ TODO: inicializar Flask Simple Login + JWT """
    app.cli.command()(list_users)
    app.cli.command()(add_user)

    admin.add_view(UserAdmin(User, db.session))