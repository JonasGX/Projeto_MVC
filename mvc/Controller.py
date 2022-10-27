from flask import Flask, render_template, request, redirect, session, flash
from Model import Model2


# Inserindo aplicação
app = Flask(__name__)

@app.route('/', methods=['GET',])
def index():
    return Model2.impimeJogos()

# Fazer a aplicação rodar
app.run(debug=True)