import sqlite3
import datetime as dt

def cad_pgt(pgt):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO pagamentos (aluno_id, mes, ano, valor) VALUES (?, ?, ?, ?)
                """, (pgt.aluno_id, pgt.mes, pgt.ano, pgt.valor))
    conn.commit()
    conn.close()
    
def listar_pgts():
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('SELECT aluno_id, mes, ano, valor FROM pagamentos')
    pgts = cur.fetchall()
    conn.close()
    return pgts

def anos_pgt(id_aluno):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT ano FROM pagamentos WHERE aluno_id = ?', (id_aluno,))
    anos = [row[0] for row in cur.fetchall()]
    conn.close()
    print(anos)
    return anos

def meses_pgt(id_aluno):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT mes FROM pagamentos WHERE aluno_id = ?', (id_aluno,))
    meses = [row[0] for row in cur.fetchall()]
    conn.close()
    return meses

def edit_pgt(valor, aluno_id, mes, ano):
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    cur.execute('UPDATE pagamentos SET valor = ? WHERE aluno_id = ? AND mes = ? AND ano = ?', (valor, aluno_id, mes, ano))
    
    rows_updated = cur.rowcount
    conn.commit()
    conn.close()
    return rows_updated

def atrasados():
    conn = sqlite3.connect("pagControl.db")
    cur = conn.cursor()
    
    mes = dt.datetime.now().month
    ano = dt.datetime.now().year

    cur.execute('''
            SELECT a.id, a.nome FROM alunos a
            WHERE NOT EXISTS (
            SELECT 1 FROM pagamentos p
            WHERE p.aluno_id = a.id AND p.mes = ? AND p.ano = ?
        )''', (mes, ano)
        ) 
    
    atrasados = cur.fetchall()
    conn.close()
    return atrasados