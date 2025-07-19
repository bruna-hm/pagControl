import sqlite3
from dao.conn_factory import executar_query

def cad_aluno(aluno):
    executar_query('INSERT INTO alunos (nome, turma) VALUES (?, ?)', (aluno.nome, aluno.turma), commit=True)

def id_aluno(nome):
    id = executar_query("SELECT id FROM alunos WHERE nome = ?", (nome,), fetchone=True)
    return id[0]

def cbb_alunos():
    return executar_query("SELECT nome FROM alunos", fetchall=True)
    
def listar_alunos():
    return executar_query('SELECT id, nome, turma FROM alunos', fetchall=True)

def anos():
    return executar_query('SELECT DISTINCT ano FROM pagamentos', fetchall=True)

def edit_aluno(turma, id):
    return executar_query('UPDATE alunos SET turma = ? WHERE id = ?', (turma, id), commit=True)

def del_aluno(id):
    return executar_query('DELETE FROM alunos WHERE id = ?', (id,), commit=True)