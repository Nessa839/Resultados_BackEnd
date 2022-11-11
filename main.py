from flask import Flask
from flask_cors import CORS
from waitress import serve
from flask import jsonify
from flask import request
import json

from Routes.Partido import partido
from Routes.Candidato import candidato
from Routes.Departamento import departamento
from Routes.Mesa import mesa
from Routes.Resultado import resultado

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(partido)
app.register_blueprint(candidato)
app.register_blueprint(departamento)
app.register_blueprint(mesa)
app.register_blueprint(resultado)


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


def loadFileConfig():
    with open('Config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])