from flask import Flask, request
""" Extensão Flask """

def init_app(app: Flask):
    """ Factory de iniciaização """

    @app.route("/")
    def index():
        print(request.args)
        return "Olá, Canganjo!"

    @app.route("/sobre")
    def sobre():
        return "Este é o melhor site de entregas"