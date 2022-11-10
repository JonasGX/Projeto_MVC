from flask import Flask, request, jsonify, make_response, render_template, redirect, flash
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


class Model2:
    # Estrutura de cadastro
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
        return render_template('lista.html', titulo='jogos', jogo=lista_jogos )

    # Estrutura de consulta
    def consultar():
        return render_template('consultar.html', titulo='jogos')
    
    def mostrarConsulta():
        return redirect('/MostrarConsulta')

    def listarConsulta():
        id = request.form['id-consulta']
        cursor = mydb.cursor()
        sql = f"SELECT * FROM jogos where id = '{id}' "
        cursor.execute(sql)
        todos_jogos = cursor.fetchall()
        cadastroJSON = json.dumps(todos_jogos)

        jogo_consultado = []
        for x in todos_jogos:
            jogo_consultado.append({
                'id': x[0],
                'nome': x[1],
                'categoria': x[2],
                'console': x[3]
            })
        return render_template('MostrarConsulta.html', titulo='Consultar Jogos', jogo=jogo_consultado )