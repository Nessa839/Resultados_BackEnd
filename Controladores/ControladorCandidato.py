from Repositorios.RepositorioCandidato import RepositorioCandidatos
from Repositorios.RepositorioPartido import RepositorioPartidos
from Models.candidatos import Candidatos
from Models.partido import Partidos


class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartidos = RepositorioPartidos()

    def index(self):
        return self.repositorioCandidatos.findAll()

    def create(self, infoCandidatos):
        nuevoCandidato = Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidatos):
        candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        candidatoActual.cedula = infoCandidatos["cedula"]
        candidatoActual.numero_resolucion = infoCandidatos["numero_resolucion"]
        candidatoActual.nombre = infoCandidatos["nombre"]
        candidatoActual.apellido = infoCandidatos["apellido"]
        return self.repositorioCandidatos.save(candidatoActual)

    def delete(self, id):
        return self.repositorioCandidatos.delete(id)

# Relación Partido y Candidato

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        partidoActual = Partidos(self.repositorioPartidos.findById(id_partido))
        candidatoActual.id_partido = partidoActual
        return self.repositorioCandidatos.save(candidatoActual)
