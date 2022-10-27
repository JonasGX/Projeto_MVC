from flask import Flask, render_template, request, redirect, session, flash
from Model import Model2


# Inserindo aplicação
app = Flask(__name__)

@app.route('/', methods=['GET',])
def index():
    return Model2.impimeJogos()

@app.route('/consulta', methods=['GET',])
def consulta():
    return Model2.consulta()

# Fazer a aplicação rodar
app.run(debug=True)