from Repositorios.RepositorioPartido import RepositorioPartidos
from Models.partido import Partidos

class ControladorPartido():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()

    def index(self):
        return self.repositorioPartidos.findAll()

    def create(self, infoPartidos):
        nuevoPartido = Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartido)

    def show(self, id):
        elPartido = Partidos(self.repositorioPartidos.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartidos):
        partidoActual = Partidos(self.repositorioPartidos.findById(id))
        partidoActual.id = infoPartidos["id"]
        partidoActual.nombre = infoPartidos["nombre"]
        partidoActual.lema = infoPartidos["lema"]
        partidoActual.candidatos = infoPartidos["candidatos"]
        return self.repositorioPartidos.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartidos.delete(id)
