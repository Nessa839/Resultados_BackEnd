from flask import Flask
from flask_cors import CORS
from waitress import serve
from flask import jsonify
from flask import request
import json

from Routes.Partido import partido
from Routes.Candidato import candidato


app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(partido)
app.register_blueprint(candidato)

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultado import ControladorResultado
from Controladores.ControladorDepartamento import ControladorDepartamento

miControlMesa = ControladorMesa()
miControlResultado = ControladorResultado()
miControlDepartamento = ControladorDepartamento()

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

###############################################################################

@app.route("/resultados", methods=['GET'])
def getResultados():
    json = miControlResultado.index()
    return jsonify(json)

@app.route("/resultados", methods=['POST'])
def crearResultados():
    data = request.get_json()
    json = miControlResultado.create(data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControlResultado.show(id)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json = miControlResultado.update(id, data)
    return jsonify(json)

@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = miControlResultado.delete(id)
    return jsonify(json)

###############################################################################
@app.route("/departamentos", methods=['GET'])
def getDepartamentos():
    json = miControlDepartamento.index()
    return jsonify(json)

@app.route("/departamentos", methods=['POST'])
def crearDepartamentos():
    data = request.get_json()
    json = miControlDepartamento.create(data)
    return jsonify(json)

@app.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = miControlDepartamento.show(id)
    return jsonify(json)

@app.route("/departamentos/<string:id>", methods=['PUT'])
def modificarDepartamentos(id):
    data = request.get_json()
    json = miControlDepartamento.update(id, data)
    return jsonify(json)

@app.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamentos(id):
    json = miControlDepartamento.delete(id)
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
