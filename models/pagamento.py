class Pagamento():
    def __init__(self, aluno_id, nome, mes, ano, valor, id=None):
        self.id = id
        self.aluno_id = aluno_id
        self.nome = nome
        self.mes = mes
        self.ano = ano
        self.valor = valor