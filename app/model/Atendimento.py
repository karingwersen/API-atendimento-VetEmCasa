from marshmallow import Schema, fields

class Atendimento:
    def __init__(self, pet: str, tutor: str, veterinario: str, data: str, horario: str, type):
        self.pet = pet
        self.tutor = tutor
        self.veterinario = veterinario
        self.data = data
        self.horario = horario
        self.type = type

    def __rpr__(self):
        return '<Atendimento(name={self.pet!r})>'.format(self=self)


class AtendimentoSchema(Schema):
    pet = fields.Str()
    tutor = fields.Str()
    veterinario = fields.Str()
    data = fields.Str()
    horario = fields.Str()
    type = fields.Str()