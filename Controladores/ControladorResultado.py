from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidatos
from Models.resultados import Resultados
from Models.mesa import Mesa
from Models.candidatos import Candidatos

class ControladorResultado():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidatos()

    def index(self):
        return self.repositorioResultados.findAll()

    def create(self, infoResultados):
        nuevoResultado = Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultado)

    def show(self, id):
        try:
            elResultado = Resultados(self.repositorioResultados.findById(id))
            return elResultado.__dict__
        except:
            response_object = {"message": 'Resultado no encontrado'}
            return "HTTP 400 Bad Request", response_object

    def update(self, id, infoResultados):
        try:
            resultadoActual = Resultados(self.repositorioResultados.findById(id))
            resultadoActual.votos = infoResultados["votos"]
            return self.repositorioResultados.save(resultadoActual)
        except:
            response_object = {"message": 'El resultado no pudo ser actualizado'}
            return "HTTP 400 Bad Request", response_object

    def delete(self,id):
        try:
            return self.repositorioResultados.delete(id)
        except:
            response_object = {"message": 'El resultado no pudo ser eliminado'}
            return "HTTP 400 Bad Request", response_object
            
# Relacion resultado-mesa y resultado-candidato

    def asignarRelacion(self, id, id_mesa, id_candidato):
        try:
            if 'id_candidato' in self.repositorioResultados.findById(id):
                condicionCandidato = self.repositorioResultados.findById(id)['id_candidato']['_id'] == id_candidato
                    
                if condicionCandidato:
                    response_object = {"message": "El candidato ya esta relacionado a un resultado"}
                    return "HTTP 409 Conflict", response_object
        
            condicionVotos = self.repositorioResultados.findById(id)['votos'] > self.repositorioMesa.findById(id_mesa)['numero_inscritos']

            if condicionVotos:
                response_object = {"message": "El numero de votos es mayor a la cantidad de inscritos"}
                return "HTTP 409 Conflict", response_object        

            resultadoActual = Resultados(self.repositorioResultados.findById(id))
            candidatoActual = Candidatos(self.repositorioCandidatos.findById(id_candidato))
            mesaActual = Mesa(self.repositorioMesa.findById(id_mesa))
            resultadoActual.id_candidato = candidatoActual
            resultadoActual.id_mesa = mesaActual
            return self.repositorioResultados.save(resultadoActual)
        except:
            response_object = {"message": 'No fue posible asignar la relacion'}
            return "HTTP 400 Bad Request", response_object
