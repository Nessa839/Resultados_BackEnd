from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Models.resultados import Resultados
from bson import ObjectId

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    pass


    def sumaVotosCandidato(self):
        query1 = {'$lookup': {'from': 'mesa', 'localField': 'id_mesa.$id', 'foreignField': '_id', 'as': 'result1'}}
        query2 = {'$lookup': {'from': 'candidatos', 'localField': 'id_candidato.$id', 'foreignField': '_id', 'as': 'result2'}}
        query3 = {'$lookup': {'from': 'partidos', 'localField': 'result2.id_partido.$id', 'foreignField': '_id', 'as': 'result3'}}
        query4 = {'$group': {'_id': {'apellido': '$result2.apellido', 'nombre': '$result2.nombre', 'partido': '$result3.nombre', 'mesa': '$result.numero_mesa'}, 'suma': {'$sum': '$votos'}}}
        query5 = {'$sort': {'suma': -1}}
        pipeline = [query1,query2,query3,query4,query5]
        return self.queryAggregation(pipeline)

    def sumaVotosMesas(self):
        query1 = {'$lookup': {'from': 'mesa', 'localField': 'id_mesa.$id', 'foreignField': '_id', 'as': 'result1'}}
        query2 = {'$group': {'_id': {'mesa': '$result1.numero_mesa'}, 'suma': {'$sum': '$votos'}}}
        query3 = {'$sort': {'suma': 1}}
        pipeline = [query1,query2,query3]
        return self.queryAggregation(pipeline)

    def sumaVotosPartidos(self):
        query1 = {'$lookup': {'from': 'candidatos', 'localField': 'id_candidato.$id', 'foreignField': '_id', 'as': 'result1'}}
        query2 = {'$lookup': {'from': 'partidos', 'localField': 'result1.id_partido.$id', 'foreignField': '_id', 'as': 'result2'}}
        query3 = {'$group': {'_id': { 'partido': '$result2.nombre'}, 'suma': {'$sum': '$votos'}}}
        query4 = {'$sort': {'suma': -1}}
        pipeline = [query1,query2,query3,query4]
        return self.queryAggregation(pipeline)

    def cuentaCongreso(self):
        query1 = {'$lookup': {'from': 'candidatos', 'localField': 'id_candidato.$id', 'foreignField': '_id', 'as': 'result1'}}
        query2 = {'$lookup': {'from': 'partidos', 'localField': 'result1.id_partido.$id', 'foreignField': '_id', 'as': 'result2'}}
        query3 = {'$group': {'_id': { 'partido': '$result2.nombre'}, 'suma': {'$count': '$votos'}}}
        query4 = {'$sort': {'suma': -1}}
        pipeline = [query1,query2,query3,query4]
        return self.queryAggregation(pipeline)