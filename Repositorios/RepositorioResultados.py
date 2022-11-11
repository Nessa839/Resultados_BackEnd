from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Models.resultados import Resultados

class RepositorioResultados(InterfaceRepositorio[Resultados]):
    pass

    def getListadoResultadosDesc(self):
        theQuery = self.baseDatos.resultados
        data = []
        for x in theQuery.find({},{"id_mesa":1, "votos":1}).sort("votos",-1):
            x["id_mesa"] = x["id_mesa"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data

    def listadoVotosDesc(self):
        query1=(

            {
                "$group": {
                    "_id": "$id_candidato",
                    "Total_votos": {
                        "$sum": "$votos"
                    }
                }
            })
        pipeline=  [query1]
        return self.queryAggregation(pipeline)

    def listadoMesas(self):
        query1=(

            {
                "$group": {
                    "_id": "$id_mesa",
                    "Total_votos": {
                        "$sum": "$votos"
                    },
                    "Total_inscritos": {
                        "$sum": "$numero_inscritos"
                    }
                }
            })
        pipeline=  [query1]
        return self.queryAggregation(pipeline)

    def getCongreso(self):
        theQuery = self.baseDatos.resultados
        data = []
        for x in theQuery.find({},{"id_mesa":1, "votos":1}).limit(15).sort("votos",-1):
            x["id_mesa"] = x["id_mesa"].__str__()
            x = self.transformObjectIds(x)
            x = self.getValuesDBRef(x)
            data.append(x)
        return data