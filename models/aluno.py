import datetime

class Aluno():
    def __init__(self, nome, turma, id=None):
        self.id = id
        self.nome = nome
        self.turma = turma
        self.pagamentos = {}
    
    def add_pagamento(self, mes, ano, valor):
        ano = datetime.now().year
        if ano not in self.pagamentos: self.pagamentos[ano] = {mes: valor}
        else: self.pagamentos[ano][mes] = valor
                
    def listar_pagamentos(self):
        return self.pagamentos