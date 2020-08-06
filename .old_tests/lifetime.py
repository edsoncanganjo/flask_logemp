#Contextos
from flask import Flask
app = Flask(__name__)
## 1 Configuração
### Add configuração
#app.config["DEBUG"] = True
#app.config["SQLALCHEMY_DB_URI"] = "mysql"

### Registar Rotas

@app.route("/path")
def funcao():
    ...

app.add_url_rule("/path", callable)

### Inicializar Extensões
from flask_admin import Admin
Admin.init_app(app)

### Registar Blueprints
app.register_blueprint(...)

### add hooks
@app.before_request(...)
@app.error_handler(...)

### Chamar outras Factories
views.init_app(app)

## 2 App Context

### App está pronto! `app`

### Testar
app.test_client
debug
objectos globais do Flask
(import Request, session, g)
- Hooks

## 3 Request Context
from flask import request, session

request.args
request.form