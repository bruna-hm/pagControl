import sqlite3

class dao():
    def __init__(self, db_path="pagControl.db"):
        self.criar_tab()

    def criar_tab(self):
        conn = sqlite3.connect('pagControl.db')
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
#        cur.execute('DELETE FROM sqlite_sequence WHERE name = "alunos" AND name = "pagamentos";')
        
        conn.commit()
        conn.close()