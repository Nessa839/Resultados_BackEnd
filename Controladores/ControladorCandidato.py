from Repositorios.RepositorioCandidato import RepositorioCandidatos
from Models.candidatos import Candidatos
class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
    def index(self):
        return self.repositorioCandidatos.findAll()
    def create(self,infoCandidatos):
        nuevoCandidato=Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidatos):
        candidatoActual=Candidatos(self.repositorioCandidatos.findById(id))
        candidatoActual.Cedula=infoCandidatos["Cedula"]
        candidatoActual.Resolucion = infoCandidatos["Resolucion"]
        candidatoActual.Nombre = infoCandidatos["Nombre"]
        candidatoActual.Apellido = infoCandidatos["Apellido"]
        return self.repositorioCandidatos.save(candidatoActual)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)