from flask import Flask, request, jsonify, make_response, render_template, redirect, flash
import json

cadastro = [
    {
        'nome': "Tetris",
        'categoria': "Puzzle",
        "console": "Atari"
    },
    {
        "nome": "God of War",
        "categoria": "Hack n Slash",
        "console": "PS2"
    },
    {
        "nome": "Mortal Kombat",
        "categoria": "Luta",
        "console": "PS2"
    }
]
cadastroJSON = json.dumps(cadastro)

class Model2:
    def impimeJogos():
        return render_template('lista.html', titulo='jogos', jogos=cadastro)

