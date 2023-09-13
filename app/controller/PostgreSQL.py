import psycopg2
from model.Atendimento import Atendimento

class PostgreSQL(object):
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __init__(self, dbname: str, user: str, password: str, host: str, port: str):
        self.create_connection(dbname=dbname, user=user, password=password, host=host, port=port)

    def create_connection(self, dbname: str, user: str, password: str, host: str, port: str):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    def create_cursor(self):
        self.cursor = self.connection.cursor()

    def listar_atendimentos(self):
        sql_statement = "select * from atendimentos;"
        self.create_cursor()
        self.cursor.execute(sql_statement)
        atendimentos = self.cursor.fetchall()

        self.close_cursor()
        self.close_connection()
        return atendimentos

    def detalhes_atendimento(self,id: str):
        sql_statement = "select * from atendimentos where id = %s;"
        self.create_cursor()
        self.cursor.execute(sql_statement, [id])
        atendimento = self.cursor.fetchone()

        self.close_cursor()
        self.close_connection()
        return atendimento

    def criar_atendimento(self, atendimento : Atendimento):
        sql_statement = "insert into atendimentos (pet, tutor, veterinario, data, horario, id) values (%s, %s, %s, %s, %s, %s);"
        self.create_cursor()
        self.cursor.execute(sql_statement,[atendimento.pet, atendimento.tutor, atendimento.veterinario, atendimento.data, atendimento.horario, atendimento.id])

        self.connection.commit()
        self.close_cursor()
        self.close_connection()
        return True

    def apagar_atendimento(self, id: str):
        sql_statement = "delete from atendimentos where id=%s;"
        self.create_cursor()
        self.cursor.execute(sql_statement, [id])

        self.connection.commit()
        self.close_cursor()
        self.close_connection()
        return True

    def atualizar_atendimento(self, atendimento: Atendimento):
        sql_statement = "update atendimentos set pet = %s, tutor = %s, veterinario = %s, data = %s, horario = %s where id=%s"
        self.create_cursor()
        self.cursor.execute(sql_statement,
                            [atendimento.pet, atendimento.tutor, atendimento.veterinario, atendimento.data,
                             atendimento.horario, atendimento.id])

        self.connection.commit()
        self.close_cursor()
        self.close_connection()
        return True

    def close_connection(self):
        self.connection.close()

    def close_cursor(self):
        self.cursor.close()