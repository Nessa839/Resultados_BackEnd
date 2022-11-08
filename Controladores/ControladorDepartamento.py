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
            return "HTTP 409 Conflict", response_object
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.repositorioDepartamento.save(nuevoDepartamento)

    def show(self, id):
        try:
            elDepartamento = Departamento(self.repositorioDepartamento.findById(id))
            return elDepartamento.__dict__
        except Exception as ed:
            response_object = {"message": 'Departamento no encontrado'}
            return "HTTP 400 Bad Request", response_object

    def update(self, id, infoDepartamento):
        try:
            departamentoActual = Departamento(self.repositorioDepartamento.findById(id))
            departamentoActual.nombre = infoDepartamento["nombre"]
            return self.repositorioDepartamento.save(departamentoActual)
        except Exception as ed:
            response_object = {"message": 'EL departamento no pudo ser actualizado'}
            return "HTTP 400 Bad Request", response_object

    def delete(self, id):
        try:
            return self.repositorioDepartamento.delete(id)
        except Exception as ed:
            response_object = {"message": 'El departamento no pudo ser eliminado'}
            return "HTTP 400 Bad Request", response_object
