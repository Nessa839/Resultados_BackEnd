from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Models.Departamento import Departamento

class ControladorDepartamento():
    def __init__(self):
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioDepartamento.findAll()

    def create(self, infoDepartamento):
        if self.repositorioDepartamento.findByKey("nombre", infoDepartamento["nombre"]):
            response_object = {"message": f"El departamento ya existe"}
            return response_object
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        try:
            elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
            return elDepartamento.__dict__
        except Exception as ed:
            response_object = {"message": 'Departamento no encontrado'}
            return response_object, 400

    def update(self, id, infoDepartamento):
        try:
            departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
            departamentoActual.nombre = infoDepartamento["nombre"]
            return self.repositorioDepartamento.save(departamentoActual)
        except Exception as ed:
            response_object = {"message": 'Departamento no pudo ser actualizado'}
            return response_object, 400

    def delete(self, id):
        try:
            return self.repositorioDepartamento.delete(id)
        except Exception as ed:
            response_object = {"message": 'Departamento no pudo ser eliminado'}
            return response_object, 400