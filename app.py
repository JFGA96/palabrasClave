import json
from flask import Flask,jsonify,request
from version4blob import calificacion

app= Flask(__name__)


@app.route('/calificaciones', methods=['POST'])
def evaluar():
    lista = request.json['list']
    claves = request.json['claves']
    respuesta = request.json['resp']
    print(lista)
    return jsonify({"calificacion":calificacion(lista,claves,respuesta)})



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True , port=4000)