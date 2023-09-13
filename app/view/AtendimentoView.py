from flask import Flask, jsonify, request
from controller.AtendimentoController import AtendimentoController
from model.Atendimento import AtendimentoSchema, Atendimento
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Atendimento API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/api/v1/listar_atendimentos")
def listar_atendimentos():
    schema = AtendimentoSchema(many=True)

    atendimentos = AtendimentoController.listar_atendimentos()

    atendimentos_response = schema.dump(atendimentos)

    return jsonify(atendimentos_response)

@app.route("/api/v1/detalhes_atendimento")
def detalhes_atendimento():
    schema = AtendimentoSchema()

    atendimento = AtendimentoController.detalhes_atendimento(request.args.get("id"))

    atendimento_response = schema.dump(atendimento)

    return jsonify(atendimento_response)

@app.route("/api/v1/criar_atendimento", methods = ["POST"])
def criar_atendimento():
    atendimento_request = request.json

    atendimento = Atendimento(pet=atendimento_request["pet"], tutor=atendimento_request["tutor"],
                              veterinario=atendimento_request["veterinario"], data=atendimento_request["data"],
                              horario=atendimento_request["horario"], id="")

    atendimento_criado = AtendimentoController.criar_atendimento(atendimento)

    if atendimento_criado:
        return "atendimento criado", 201
    else:
        return "atendimento não criado", 500

@app.route("/api/v1/apagar_atendimento", methods = ["DELETE"])
def apagar_atendimento():

    atendimento_deletado = AtendimentoController.apagar_atendimento(request.args.get("id"))

    if atendimento_deletado:
        return "atendimento deletado", 204
    else:
        return "atendimento não deletado", 500

@app.route("/api/v1/atualizar_atendimento", methods = ["PUT"])
def atualizar_atendimento():
    atendimento_request = request.json

    atendimento = Atendimento(pet=atendimento_request["pet"], tutor=atendimento_request["tutor"],
                              veterinario=atendimento_request["veterinario"], data=atendimento_request["data"],
                              horario=atendimento_request["horario"], id=request.args.get("id"))

    atendimento_atualizado = AtendimentoController.atualizar_atendimento(atendimento)

    if atendimento_atualizado:
        return "atendimento atualizado", 202
    else:
        return "atendimento não atualizado", 500

def atendimento_view():
    app.run(host="0.0.0.0", port=5000)
