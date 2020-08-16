import click
from maisqfood.ext.auth.models import User
from maisqfood.ext.db import db #noqa

def list_users():
    users = User.query.all()
    click.echo(f"lista de usuários {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """Adiciona novo usuário """
    user = User(
    email=email,
    passwd=passwd,
    admin=admin
    )
    db.session.add(user)
    db.session.commit()

    click.echo(f"Usuário {email} criado com sucesso!")