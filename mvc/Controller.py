from flask import Flask, render_template, request, redirect, session, flash
from Model import Model2

# Inserindo aplicação
app = Flask(__name__)

@app.route('/',)
def novo():
    return Model2.novoJogo()

@app.route('/jogos', methods=['GET',])
def index():
    return Model2.impimeJogos()

# ---------- Estrutura criacao
@app.route('/criar', methods=['POST',])
def criar():
    return Model2.cadastrarJogo()

@app.route('/bd', methods=['GET',])
def bancodados():
    return Model2.cadastrarJogo()

# ---------- Estrutura consulta
@app.route('/realizarconsulta', methods=['GET',])
def consulta():
    return Model2.consultar()

@app.route('/MostrarConsulta', methods=['GET',])
def criarconsulta():
    return Model2.mostrarConsulta()

@app.route('/criarconsulta', methods=['POST',])
def listarconsulta():
    return Model2.listarConsulta()


# Fazer a aplicação rodar
app.run(debug=True)