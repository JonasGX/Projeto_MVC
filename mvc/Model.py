from flask import Flask, request, jsonify, make_response, render_template, redirect, flash
import json

cadastro = [
    {
        "id": 50,
        'nome': "Tetris",
        'categoria': "Puzzle",
        "console": "Atari"
    },
    {
        "id": 2,
        "nome": "God of War",
        "categoria": "Hack n Slash",
        "console": "PS2"
    },
    {
        "id": 1000,
        "nome": "Mortal Kombat",
        "categoria": "Luta",
        "console": "PS2"
    }
]

cadastroJSON = json.dumps(cadastro)

class Model2:
    def impimeJogos():
        lista1 = []
        lista2 = []
        for x in cadastro:
            if x["id"] >= 1 and x["id"] <= 10:
                lista1.append(x) 
            else:
                lista2.append(x)
        return render_template('lista.html', titulo='jogos', jogos1=lista1, jogos2=lista2)
