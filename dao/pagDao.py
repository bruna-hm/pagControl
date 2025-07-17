import sqlite3
import datetime as dt
from dao.conn_factory import executar_query

def cad_pgt(pgt):
    return executar_query(
                    "INSERT INTO pagamentos (aluno_id, mes, ano, valor) VALUES (?, ?, ?, ?)",
                    (pgt.aluno_id, pgt.mes, pgt.ano, pgt.valor),
                    commit=True
                )
    
def listar_pgts():
    return executar_query('SELECT aluno_id, mes, ano, valor FROM pagamentos',
                          fetchall=True)

def anos_pgt(id_aluno):
    anos = executar_query('SELECT DISTINCT ano FROM pagamentos WHERE aluno_id = ?', (id_aluno,), 
                   fetchall=True)
    return [row[0] for row in anos]

def meses_pgt(id_aluno):
    meses = executar_query('SELECT DISTINCT mes FROM pagamentos WHERE aluno_id = ?', (id_aluno,))
    return [row[0] for row in meses]

def edit_pgt(valor, aluno_id, mes, ano):
    return executar_query('UPDATE pagamentos SET valor = ? WHERE aluno_id = ? AND mes = ? AND ano = ?', 
                (valor, aluno_id, mes, ano),
                commit = True,
                rowcount=True
                )

def atrasados():
    mes = dt.datetime.now().month
    ano = dt.datetime.now().year
    
    return executar_query('''
            SELECT a.id, a.nome FROM alunos a
            WHERE NOT EXISTS (
            SELECT 1 FROM pagamentos p
            WHERE p.aluno_id = a.id AND p.mes = ? AND p.ano = ?
            )''',
            (mes, ano),
            fetchall=True
        ) 