import sqlite3


def cad_aluno(aluno):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO alunos (nome, turma) VALUES (?, ?)',
                (aluno.nome, aluno.turma))
    conn.commit()
    conn.close()

def id_aluno(nome):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM alunos WHERE nome = ?", (nome,))
    id = cur.fetchone()
    conn.close()
    return id[0]

def cbb_alunos():
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute("SELECT nome FROM alunos")
    nomes = cur.fetchall()
    conn.close()
    return nomes
    
def listar_alunos():
    conn = sqlite3.connect("pagCOntrol.db")
    cur = conn.cursor()
    cur.execute('SELECT id, nome, turma FROM alunos')
    alunos = cur.fetchall()
    conn.close()
    return alunos

def anos():
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT ano FROM pagamentos')
    anos = cur.fetchall()
    conn.close()
    return anos

def edit_aluno(turma, id):
    conn = sqlite3.connect("pagCOntrol.db")
    cur = conn.cursor()
    cur.execute('UPDATE alunos SET turma = ? WHERE id = ?', (turma, id))
    
    conn.commit()
    conn.close()

def del_aluno(id):
    conn = sqlite3.connect("pagCOntrol.db")
    cur = conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute('DELETE FROM alunos WHERE id = ?', (id,))
    
    conn.commit()
    conn.close()