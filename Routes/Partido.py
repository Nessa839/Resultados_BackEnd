from flask import jsonify, request, Blueprint
from Controladores.ControladorPartido import ControladorPartido

miControladorPartido = ControladorPartido()
partido = Blueprint('partido', __name__)


@partido.route("/partidos", methods=['GET'])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)


@partido.route("/partidos", methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@partido.route("/partidos/<string:id>", methods=['GET'])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@partido.route("/partidos/<string:id>", methods=['PUT'])
def modificarPartidos(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@partido.route("/partidos/<string:id>", methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)
