from flask import jsonify, request, Blueprint
from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato = ControladorCandidato()
candidato = Blueprint('candidato', __name__)


@candidato.route("/candidatos", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@candidato.route("/candidatos", methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)


@candidato.route("/candidatos/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)


@candidato.route("/candidatos/<string:id>", methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)


@candidato.route("/candidatos/<string:id>", methods=['DELETE'])
def eliminarCandidatos(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)


@candidato.route("/candidatos/<string:id>/partidos/<string:id_partido>", methods=['PUT'])
def asignarPartido(id, id_partido):
    json = miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)
