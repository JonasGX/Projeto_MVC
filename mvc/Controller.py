from flask import Flask, render_template, request, redirect, session, flash
from Model import Model

# Inserindo aplicação
app = Flask(__name__)

@app.route('/',)
def novo():
    return Model.novoJogo()

@app.route('/jogos', methods=['GET',])
def index():
    return Model.impimeJogos()

# ---------- Estrutura criacao
@app.route('/criar', methods=['POST',])
def criar():
    return Model.cadastrarJogo()

# ---------- Estrutura consulta
@app.route('/realizarconsulta', methods=['GET',])
def consulta():
    return Model.consultar()

@app.route('/MostrarConsulta', methods=['GET',])
def criarconsulta():
    return Model.mostrarConsulta()

@app.route('/criarconsulta', methods=['POST',])
def listarconsulta():
    return Model.listarConsulta()


# Fazer a aplicação rodar
app.run(debug=True)