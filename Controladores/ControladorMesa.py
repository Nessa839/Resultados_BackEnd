from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Models.mesa import Mesa
from Models.Departamento import Departamento

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        if self.repositorioMesa.findByKey("numero_mesa", infoMesa["numero_mesa"]):
            response_object = {"message": "La mesa ya existe"}
            return "HTTP 409 Conflict", response_object
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        try:
            laMesa = Mesa(self.repositorioMesa.findById(id))
            return laMesa.__dict__
        except Exception as e:
            response_object = {"message": 'Mesa no encontrada'}
            return "HTTP 400 Bad Request", response_object

    def update(self, id, infoMesa):
        try:
            mesaActual = Mesa(self.repositorioMesa.findById(id))
            mesaActual.numero_mesa = infoMesa["numero_mesa"]
            mesaActual.numero_inscritos = infoMesa["numero_inscritos"]
            return self.repositorioMesa.save(mesaActual)
        except Exception as ex:
            response_object = {"message": 'La mesa no pudo ser actualizada'}
            return "HTTP 400 Bad Request", response_object

    def delete(self, id):
        try:
            return self.repositorioMesa.delete(id)
        except Exception as ed:
            response_object = {"message": 'La mesa no pudo ser eliminada'}
            return "HTTP 400 Bad Request", response_object

# Relacion departamento y mesa
    
    def asignarDepartamento(self, id, id_departamento):
        try:
            mesaActual = Mesa(self.repositorioMesa.findById(id))
            departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
            mesaActual.id_departamento = departamentoActual
            return self.repositorioMesa.save(mesaActual)
        except:
            response_object = {"message": 'No fue posible asignar la relacion'}
            return "HTTP 400 Bad Request", response_object
