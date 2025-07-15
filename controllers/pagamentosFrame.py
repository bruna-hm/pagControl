import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import datetime as dt
from models.pagamento import Pagamento
from views.utils import mes_pt, inv_mes, resource_path
from dao.pagDao import cad_pgt
from dao.alunoDao import cbb_alunos, id_aluno

class pagamentoFrame(tk.Toplevel):
    def __init__(self, master=None, atualizar_atrasados=None):
        super().__init__(master)
        self.iconbitmap(default=resource_path("assets/img/dojo.ico"))    
        self.atualizar_atrasados = atualizar_atrasados
        self.title("Bunshin Dojo")
        self.title("Registro de pagamento")
        self.resizable(False, False)
        
        largura = 300
        altura = 300
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = ((altura_tela - altura) // 2) - 50
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        
        self.create_widgets()
        
    def create_widgets(self):
        style = ttk.Style()
        style.configure("Formulario.TLabel", font=("Segoe Ui", 12))
        
        nome_lbl = ttk.Label(self, text="Nome:", style="Formulario.TLabel")
        nome_lbl.place(x=30, y=20)  
        nome_cbb = ttk.Combobox(self, width=35)
        nome_cbb['values'] = [nome[0] for nome in cbb_alunos()]
        nome_cbb.place(x=30, y=50)
        
        style.configure("Formulario.TEntry", font=("Segoe Ui", 20),  padding=5)
        mes_lbl = ttk.Label(self, text="Mês:", style="Formulario.TLabel")
        mes_lbl.place(x=36, y=105)
        mes_cbb = ttk.Combobox(self)
        mes_cbb['values'] = [mes_pt(mes) for mes in range(1, 13)]
        mes_cbb.place(x=98, y=110)
        
        style.configure("Formulario.TEntry", font=("Consolas", 12))
        valor_lbl = ttk.Label(self, text="Valor:", style="Formulario.TLabel")
        valor_lbl.place(x=30, y=160)
        valor_ety = ttk.Entry(self, width=22, style="Formulario.TEntry")
        valor_ety.place(x=98, y=160)
        
        date = dt.datetime.now()
        ano = date.year
        style.configure("Formulario.TButton", font=("Segoe Ui SemiBold", 14), padding=6)
        cdt_btn = ttk.Button(self, text="Cadastrar", style="Formulario.TButton",
                     command=lambda: self.registrar_pgt(nome_cbb.get(), mes_cbb.get(), ano, valor_ety.get()))
        cdt_btn.place(x=80, y=220)
        
    def registrar_pgt(self, nome, mes, ano, valor):
 
        if not nome or not mes or not ano or  not valor:
            messagebox.showerror("Erro", "Campo em Branco, verifique as informações!")
        else:
            aluno_id = id_aluno(nome)
            pgt = Pagamento(aluno_id, nome, inv_mes(mes), ano, float(valor))
            cad_pgt(pgt)
            if self.atualizar_atrasados:
                self.atualizar_atrasados()
            self.destroy()