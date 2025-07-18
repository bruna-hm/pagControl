import sqlite3
        
def executar_query(query, params=(), rowcount=False, fetchall=False, fetchone=False, commit=False):
     with sqlite3.connect("pagControl.db") as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute(query, params)

        if commit:
            conn.commit()
        if rowcount:
            return cur.rowcount()
        if fetchone:
            return cur.fetchone()
        elif fetchall:
            return cur.fetchall()
            
        
def criar_tab():
    with sqlite3.connect("pagControl.db") as conn:
        cur = conn.cursor()    
    
    cur.execute("PRAGMA foreign_keys = ON;")
        
    cur.execute('''CREATE TABLE IF NOT EXISTS alunos 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                     nome VARCHAR(100) NOT NULL, 
                     turma VARCHAR(100) NOT NULL);
                     ''')
        
    cur.execute('''CREATE TABLE IF NOT EXISTS pagamentos 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_id INTEGER NOT NULL,
                    mes INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    valor REAL DEFAULT 0,
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE);
                    ''')

#Retirar a hashtag abaixo para zerar contagem de ids em autoincrement no banco de dados
#    cur.execute('DELETE FROM sqlite_sequence WHERE name = "alunos" AND name = "pagamentos";')
        
    conn.commit()
    conn.close()