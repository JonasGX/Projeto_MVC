from flask import Flask, render_template, request, redirect, session, flash
from Model import Model

# Inserindo aplicação
app = Flask(__name__)
app.secret_key = 'jonasgx'

# ---------- Estrutura criacao
@app.route('/',)
def cadastrocliente():
    return Model.cadastro()

@app.route('/novoJogo',)
def novoJogo():
    return Model.novoJogo()

@app.route('/criar', methods=['POST',])
def criar():
    return Model.cadastrarJogo()

@app.route('/jogos', methods=['GET',])
def index():
    return Model.impimeJogos()

# ---------- Estrutura consulta
@app.route('/realizarconsulta', methods=['GET',])
def consulta():
    return Model.consultar()

@app.route('/criarconsulta', methods=['POST',])
def listarconsulta():
    return Model.listarConsulta()

@app.route('/MostrarConsulta', methods=['GET',])
def criarconsulta():
    return Model.mostrarConsulta()


# ---------- Estrutura de autenticação do cadastro cliente
@app.route('/cadastrarUsuario')
def paginacadastro():
    return render_template('cadastroCliente.html')

@app.route('/autenticarCadastro', methods=['POST',])
def cadastrar():
    return Model.cadastrarCliente()

# ---------- Estrutura de autenticação do login cliente
@app.route('/login')
def paginalogin():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def logar():
    return Model.autenticar()

# Fazer a aplicação rodar
app.run(debug=True)