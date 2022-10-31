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
        nuevaMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero_mesa = infoMesa["numero_mesa"]
        mesaActual.departamento = infoMesa["departamento"]
        mesaActual.inscritos = infoMesa["inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        return self.repositorioMesa.delete(id)

    """
    Relacion departamento y mesa
    """
    def asignarDepartamento(self, id, id_departamento):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        mesaActual.id_departamento = departamentoActual
        return self.repositorioMesa.save(mesaActual)