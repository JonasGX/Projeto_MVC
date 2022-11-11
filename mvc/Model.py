from flask import Flask, request, jsonify, make_response, render_template, redirect, flash, session
import json
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Acordeon2002$',
    database='jogoteca'
)


cursor = mydb.cursor()
sql = f"SELECT * FROM usuarios where senha = '1234' "
cursor.execute(sql)
senha = cursor.fetchall()

dicts = {}
for x in senha:
    dicts = {
        'cpf': x[0],
        'nome_usuario': x[1],
        'senha': x[2]
    }
set_dados = dicts.setdefault('cpf')

print(set_dados)

class Model:
    # Estrutura de cadastro do jogo
    def cadastro():
        if 'usuario_logado' not in session or session['usuario_logado'] == None:
            return redirect('/cadastrarUsuario')
        return render_template('cadastroCliente.html', titulo='jogos')

    def novoJogo():
        return render_template('novo.html', titulo='jogos')

    def cadastrarJogo():
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']

        cursor = mydb.cursor()
        sql = f"INSERT INTO jogos (nome, categoria, console) VALUES('{nome}','{categoria}', '{console}')"
        cursor.execute(sql)
        mydb.commit()
        cursor.close()

        return redirect('/jogos')

    # Estrutura para mostrar os Jogos
    def impimeJogos():
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM jogos')
        todos_jogos = cursor.fetchall()

        lista_jogos = []
        for x in todos_jogos:
            lista_jogos.append({
                'id': x[0],
                'nome': x[1],
                'categoria': x[2],
                'console': x[3]
            })
        return render_template('lista.html', titulo='jogos', jogo=lista_jogos)

    # Estrutura de consulta dos Jogos
    def consultar():
        return render_template('consultar.html', titulo='jogos')

    def mostrarConsulta():
        return redirect('/MostrarConsulta')

    def listarConsulta():
        id = request.form['id-categoria']
        cursor = mydb.cursor()
        sql = f"SELECT * FROM jogos where categoria = '{id}' "
        cursor.execute(sql)
        todos_dados = cursor.fetchall()

        jogo_consultado = []
        for x in todos_dados:
            jogo_consultado.append({
                'id': x[0],
                'nome': x[1],
                'categoria': x[2],
                'console': x[3]
            })
        return render_template('consultar.html', titulo='Consultar Jogos', jogo=jogo_consultado)

    # Estrutura de autenticação do cadastro cliente
    def cadastrarCliente():
        cpf = request.form['cpf']
        nome_usuario = request.form['nome_usuario']
        senha = request.form['senha']

        cursor = mydb.cursor()
        sql = f"INSERT INTO usuarios (cpf, nome_usuario, senha) VALUES('{cpf}', '{nome_usuario}', '{senha}')"
        cursor.execute(sql)
        mydb.commit()
        cursor.close()

        return redirect('/login')

    # Estrutura de autenticação do login cliente
    def login():
        return render_template('login.html')

    def autenticar():
        senhaBrowser = request.form['senhaLogin']
        cursor = mydb.cursor()
        sql = f"SELECT * FROM usuarios where senha = '{senhaBrowser}' "
        cursor.execute(sql)
        senha = cursor.fetchall()

        dicts = {}
        for x in senha:
            dicts = {
                'cpf': x[0],
                'nome_usuario': x[1],
                'senha': x[2]
            }
        set_dados_senha = dicts.setdefault('senha')
        set_dados_cpf = dicts.setdefault('cpf')

        if set_dados_senha == request.form['senhaLogin'] and set_dados_cpf == request.form['cpfLogin']:
            # session deixa os dados guardados nos cookies da página
            # Armazena o nome do usuario nessa chave
            session['usuario_logado'] = 'Usuario'
            flash(f"{session['usuario_logado']} logado com sucesso!")
            return redirect('/jogos')
        else:
            flash('Usuário não logado')
            return redirect('/login')
