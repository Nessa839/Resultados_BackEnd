from flask import jsonify,request,Blueprint
from Controladores.ControladorMesa import ControladorMesa

miControlMesa = ControladorMesa()

mesa = Blueprint('mesa', __name__)

@mesa.route("/mesas", methods=['GET'])
def getMesas():
    json = miControlMesa.index()
    return jsonify(json)

@mesa.route("/mesas", methods=['POST'])
def crearMesas():
    data = request.get_json()
    json = miControlMesa.create(data)
    return jsonify(json)

@mesa.route("/mesas/<string:id>", methods=['GET'])
def getMesa(id):
    json = miControlMesa.show(id)
    return jsonify(json)

@mesa.route("/mesas/<string:id>", methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json = miControlMesa.update(id, data)
    return jsonify(json)

@mesa.route("/mesas/<string:id>", methods=['DELETE'])
def eliminarMesas(id):
    json = miControlMesa.delete(id)
    return jsonify(json)

@mesa.route("/mesas/<string:id>/departamentos/<string:id_departamento>", methods=['PUT'])
def asignarDepartamentoMesa(id, id_departamento):
    json = miControlMesa.asignarDepartamento(id,id_departamento)
    return jsonify(json)