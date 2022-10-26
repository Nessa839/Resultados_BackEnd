from Repositorios.RepositorioResultados import RepositorioResultados
from Models.resultados import Resultados

class ControladorResultado():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self, infoResultados):
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultados):
        resultadoActual = Resultados(self.repositorioResultados.findById(id))
        resultadoActual.mesa = infoResultados["mesa"]
        resultadoActual.votos = infoResultados["votos"]
        return self.repositorioResultados.save(resultadoActual)

    def delete(self,id):
        return self.repositorioResultados.delete(id)
