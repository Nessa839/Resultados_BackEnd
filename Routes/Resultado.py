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
    return jsonify(json)


@resultado.route("/resultados/<string:id>/mesas/<string:id_mesa>/candidatos/<string:id_candidato>", methods=['PUT'])
def asignarRelacion(id, id_mesa, id_candidato):
    json = miControladorResultado.asignarRelacion(id, id_mesa, id_candidato)
    return jsonify(json)
