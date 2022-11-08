from Repositorios.RepositorioPartido import RepositorioPartidos
from Models.partido import Partidos


class ControladorPartido():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()

    def index(self):
        return self.repositorioPartidos.findAll()

    def create(self, infoPartidos):
        if self.repositorioPartidos.findByKey("nombre", infoPartidos["nombre"]):
            response_object = {"message": "El partido ya existe"}
            return "HTTP 409 Conflict", response_object
        nuevoPartido = Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartido)

    def show(self, id):
        try:
            elPartido = Partidos(self.repositorioPartidos.findById(id))
            return elPartido.__dict__
        except Exception as ed:
            response_object = {"message": 'Partido no encontrado'}
            return "HTTP 400 Bad Request", response_object

    def update(self, id, infoPartidos):
        try:
            partidoActual = Partidos(self.repositorioPartidos.findById(id))
            partidoActual.nombre = infoPartidos["nombre"]
            partidoActual.lema = infoPartidos["lema"]
            return self.repositorioPartidos.save(partidoActual)
        except Exception as ed:
            response_object = {"message": 'El partido no pudo ser actualizado'}
            return "HTTP 400 Bad Request", response_object

    def delete(self, id):
        try:
            return self.repositorioPartidos.delete(id)
        except Exception as ed:
            response_object = {"message": 'El partido no pudo ser eliminado'}
            return "HTTP 400 Bad Request", response_object
