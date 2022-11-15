from flask import jsonify, request, Blueprint
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado = ControladorResultado()
resultado = Blueprint('resultado', __name__)


@resultado.route("/resultados", methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@resultado.route("/resultados", methods=['POST'])
def crearResultados():
    data = request.get_json()
    json = miControladorResultado.create(data)
    return jsonify(json)


@resultado.route("/resultados/<string:id>", methods=['GET'])
def getResultado(id):
    json = miControladorResultado.show(id)
    return jsonify(json)


@resultado.route("/resultados/<string:id>", methods=['PUT'])
def modificarResultados(id):
    data = request.get_json()
    json = miControladorResultado.update(id, data)
    return jsonify(json)


@resultado.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultados(id):
    json = miControladorResultado.delete(id)
    return (json)


@resultado.route("/resultados/<string:id>/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods=['PUT'])
def asignarRelacion(id, id_mesa, id_candidato):
    json = miControladorResultado.asignarRelacion(id, id_mesa, id_candidato)
    return jsonify(json)

# Muestra resultado de las votaciones por mesa__________________________________________________
@resultado.route("/resultados/votos",methods=['GET'])
def getSumaVotosCandidatos():
    json=miControladorResultado.VotosCandidatos()
    return jsonify(json)

@resultado.route("/resultados/mesas",methods=['GET'])
def getSumaVotosMesas():
    json=miControladorResultado.VotosMesa()
    return jsonify(json)

@resultado.route("/resultados/partidos",methods=['GET'])
def getVotosPartido():
    json=miControladorResultado.votosPartidos()
    return jsonify(json)

@resultado.route("/resultados/congreso",methods=['GET'])
def getCongreso():
    json=miControladorResultado.congreso()
    return jsonify(json)