from marshmallow import Schema, fields
from datetime import datetime as dt

class Atendimento(object):
    def __init__(self, pet: str, tutor: str, veterinario: str, data: dt.date, horario: dt.time, id: str):
        self.pet = pet
        self.tutor = tutor
        self.veterinario = veterinario
        self.data = data
        self.horario = horario
        self.id = id

    def __rpr__(self):
        return '<Atendimento(name={self.pet!r})>'.format(self=self)


class AtendimentoSchema(Schema):
    pet = fields.Str()
    tutor = fields.Str()
    veterinario = fields.Str()
    data = fields.Date()
    horario = fields.Time()
    id = fields.Str()