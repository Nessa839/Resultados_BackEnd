from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido

miControlMesa = ControladorMesa()
miControlCandidato = ControladorCandidato()
miControlPartido = ControladorPartido()

#################################################################################
@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)
################################################################################
@app.route("/mesas", methods=['GET'])
def getMesas():
    json = miControlMesa.index()
    return jsonify(json)
@app.route("/mesas", methods=['POST'])
def crearMesas():
    data = request.get_json()
    json = miControlMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControlMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json = miControlMesa.update(id, data)
    return jsonify(json)
@app.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesas(id):
    json = miControlMesa.delete(id)
    return jsonify(json)

#################################################################################
@app.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControlCandidato.index()
    return jsonify(json)
@app.route("/candidatos", methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json = miControlCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControlCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json = miControlCandidato.update(id, data)
    return jsonify(json)
@app.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidatos(id):
    json = miControlCandidato.delete(id)
    return jsonify(json)
###############################################################################
@app.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControlPartido.index()
    return jsonify(json)
@app.route("/partidos", methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json = miControlPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControlPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json = miControlPartido.update(id, data)
    return jsonify(json)
@app.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControlPartido.delete(id)
    return jsonify(json)
###############################################################################
def loadFileConfig():
    with open('Config.json') as f:
        data = json.load(f)
    return data
if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])