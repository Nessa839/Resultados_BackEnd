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
        if self.repositorioCandidatos.findByKey("cedula", infoCandidatos["cedula"]):
            response_object = {"message": "La cedula ya esta asociada a un candidato"}
            return "HTTP 409 Conflict", response_object
        
        if self.repositorioCandidatos.findByKey("numero_resolucion", infoCandidatos["numero_resolucion"]):
            response_object = {"message": "El numero de resolucion ya esta asociado a un candidato"}
            return "HTTP 409 Conflict", response_object

        nuevoCandidato = Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato) 

    def show(self, id):
        try:
            elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
            return elCandidato.__dict__
        except:
            response_object = {"message": 'Candidato no encontrado'}
            return "HTTP 400 Bad Request", response_object

    def update(self, id, infoCandidatos):
        try:
            candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
            candidatoActual.cedula = infoCandidatos["cedula"]
            candidatoActual.numero_resolucion = infoCandidatos["numero_resolucion"]
            candidatoActual.nombre = infoCandidatos["nombre"]
            candidatoActual.apellido = infoCandidatos["apellido"]
            return self.repositorioCandidatos.save(candidatoActual)
        except:
            response_object = {"message": 'El candidato no pudo ser actualizado'}
            return "HTTP 400 Bad Request", response_object

    def delete(self, id):
        try:
            return self.repositorioCandidatos.delete(id)
        except:
            response_object = {"message": 'El candidato no pudo ser eliminado'}
            return "HTTP 400 Bad Request", response_object

# Relación Partido y Candidato

    def asignarPartido(self, id, id_partido):
        try:
            candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
            partidoActual = Partidos(self.repositorioPartidos.findById(id_partido))
            candidatoActual.id_partido = partidoActual
            return self.repositorioCandidatos.save(candidatoActual)
        except:
            response_object = {"message": 'No fue posible asignar la relacion'}
            return "HTTP 400 Bad Request", response_object
