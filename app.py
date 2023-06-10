# pip install Flask
from flask import Flask, render_template
app = Flask(__name__)

# 1. routes (endpoint = URL)
# ex.: https://casasbahia.com/contato
# 2. function executa uma solicitação do route
# 3. templates (design da tela solicitada)

# rota da página principal
# home page = domínio do site
# ex.: / == https://casasbahia.com
# Rodando local = http://127.0.0.1:5000/
# Rodando local = localhost:5000/

@app.route("/")
def homepage():
    return render_template("index.html")

# rota de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# rota de usuários
@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

if __name__ == "__main__":
  app.run(debug=True)