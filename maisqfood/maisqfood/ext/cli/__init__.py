from maisqfood.ext.db import db

def init_app(app):
    @app.cli.command()
    def create_db():
        """ Este comando inicializa o db """
        try:
            db.create_all()

@app.cli.command()
    def listar_pedidos():
        return "lista de pedidos"

@app.cli.command()
    def listar_usuarios():
        return "lista de usuarios"
