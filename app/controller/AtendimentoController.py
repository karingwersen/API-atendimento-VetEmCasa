from controller.PostgreSQL import PostgreSQL
from model.Atendimento import Atendimento

class AtendimentoController:

    @staticmethod
    def listar_atendimentos():
        postgresql = PostgreSQL()
        atendimentos_info = postgresql.listar_atendimentos()

        atendimentos = []

        for atendimento_info in atendimentos_info:
            atendimento = Atendimento(pet=atendimento_info[0], tutor=atendimento_info[1],
                                      veterinario=atendimento_info[2], data=atendimento_info[3],
                                      horario=atendimento_info[4], id=atendimento_info[5])
            atendimentos.append(atendimento)

        return atendimentos



    @staticmethod
    def detalhes_atendimento(id: str):
        postgresql = PostgreSQL()
        atendimento_info = postgresql.detalhes_atendimento(id)

        atendimento = Atendimento(pet=atendimento_info[0], tutor=atendimento_info[1], veterinario=atendimento_info[2],
                                 data=atendimento_info[3], horario=atendimento_info[4], id=atendimento_info[5])

        return atendimento

    @staticmethod
    def criar_atendimento(atendimento : Atendimento):
        postgresql = PostgreSQL()
        resultado = postgresql.criar_atendimento(atendimento)

        if resultado:
            return True
        else:
            return False