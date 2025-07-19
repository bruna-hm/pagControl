import datetime

class Aluno():
    def __init__(self, nome, turma, id=None):
        self.id = id
        self.nome = nome
        self.turma = turma
        self.pagamentos = {}