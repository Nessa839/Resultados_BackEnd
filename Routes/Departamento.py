from flask import jsonify,request,Blueprint
from Controladores.ControladorDepartamento import ControladorDepartamento

miControlDepartamento = ControladorDepartamento()

departamento = Blueprint('departamento', __name__)

@departamento.route("/departamentos", methods=['GET'])
def getDepartamentos():
    json = miControlDepartamento.index()
    return jsonify(json)

@departamento.route("/departamentos", methods=['POST'])
def crearDepartamentos():
    data = request.get_json()
    json = miControlDepartamento.create(data)
    return jsonify(json)

@departamento.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = miControlDepartamento.show(id)
    return jsonify(json)

@departamento.route("/departamentos/<string:id>", methods=['PUT'])
def modificarDepartamentos(id):
    data = request.get_json()
    json = miControlDepartamento.update(id, data)
    return jsonify(json)

@departamento.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamentos(id):
    json = miControlDepartamento.delete(id)
    return jsonify(json)
