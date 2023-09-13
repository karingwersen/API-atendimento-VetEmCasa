from controller.PostgreSQL import PostgreSQL
from model.Atendimento import Atendimento
import random

class AtendimentoController:

    @staticmethod
    def listar_atendimentos():
        postgresql = PostgreSQL(dbname="vetemcasa", user="postgres", password="", host="localhost", port="5432")
        atendimentos_info = postgresql.listar_atendimentos()

        atendimentos = []

        for atendimento_info in atendimentos_info:
            atendimento = Atendimento(pet=atendimento_info[0], tutor=atendimento_info[1],
                                      veterinario=atendimento_info[2], data=atendimento_info[4],
                                      horario=atendimento_info[5], id=atendimento_info[3])
            atendimentos.append(atendimento)

        return atendimentos



    @staticmethod
    def detalhes_atendimento(id: str):
        postgresql = PostgreSQL(dbname="vetemcasa", user="postgres", password="", host="localhost", port="5432")
        atendimento_info = postgresql.detalhes_atendimento(id)

        atendimento = Atendimento(pet=atendimento_info[0], tutor=atendimento_info[1], veterinario=atendimento_info[2],
                                 data=atendimento_info[4], horario=atendimento_info[5], id=atendimento_info[3])

        return atendimento

    @staticmethod
    def criar_atendimento(atendimento : Atendimento):
        postgresql = PostgreSQL(dbname="vetemcasa", user="postgres", password="", host="localhost", port="5432")
        hash = random.getrandbits(128)
        id = "%032x" % hash
        atendimento.id = id
        resultado = postgresql.criar_atendimento(atendimento)

        if resultado:
            return True
        else:
            return False

    @staticmethod
    def apagar_atendimento(id: str):
        postgresql = PostgreSQL(dbname="vetemcasa", user="postgres", password="", host="localhost", port="5432")

        resultado = postgresql.apagar_atendimento(id)

        if resultado:
            return True
        else:
            return False

    @staticmethod
    def atualizar_atendimento(atendimento: Atendimento):
        postgresql = PostgreSQL(dbname="vetemcasa", user="postgres", password="", host="localhost", port="5432")

        resultado = postgresql.atualizar_atendimento(atendimento)

        if resultado:
            return True
        else:
            return False