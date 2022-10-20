from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)


@app.route('/v1/aula/cadastrar', methods=["POST"])
def cadastrar():
     input_json = request.get_json(force=True) 
     #camada de banco de dados
     jsonToReturn = {'nome':input_json['nome'], 'Cadastro':'Efetuado com sucesso'}
     return jsonify(jsonToReturn), 200


@app.route('/v1/aula/consultar/', methods=["GET"])
def consultar():
    jsonToReturn = {'id':'1', 'name':'Alexandre'}, {'id':'2', 'name':'João'}
    return jsonToReturn
    #return jsonify(list(range(5)))
    #return 'primeira chamada de api!'




















#http://localhost:5000/v1/aula/deletar/5
@app.route('/v1/aula/deletar/<int:number>/', methods=["DELETE"])
def deletar(number):
     return "Excluido " + str(number)
     #return "Excluido " + str(number), 401
















































@app.route('/v1/aula/atualizar', methods=["PUT"])
def atualizar():
     input_json = request.get_json(force=True) 
     #banco de dados
     jsonToReturn = {'text':input_json['text'], 'text2':input_json['text2']}
     return jsonify(jsonToReturn)









if __name__ == '__main__':
    app.run(debug=True,port= 5001)