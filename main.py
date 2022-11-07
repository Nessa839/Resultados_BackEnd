from flask import Flask
from flask_cors import CORS
from waitress import serve
from flask import jsonify
from flask import request
import json

from Routes.Partido import partido
from Routes.Candidato import candidato
from Routes.Departamento import departamento
from Routes.Mesa import mesa

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(partido)
app.register_blueprint(candidato)
app.register_blueprint(departamento)
app.register_blueprint(mesa)

from Controladores.ControladorResultado import ControladorResultado

miControlResultado = ControladorResultado()

#################################################################################

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)

################################################################################

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

def loadFileConfig():
    with open('Config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
