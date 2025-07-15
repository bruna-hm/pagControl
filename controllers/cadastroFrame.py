import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from models.aluno import Aluno
from dao.alunoDao import cad_aluno
from views.utils import resource_path

class cadastroFrame(tk.Toplevel):
    def __init__(self, master=None, atualizar_atrasados=None):
        super().__init__(master)
        self.withdraw()
        icon_path = resource_path("assets/img/dojo.png")
        icon = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon)
        self.atualizar_atrasados = atualizar_atrasados
        self.title("Bunshin Dojo")
        self.title("Cadastro de Aluno")
        self.resizable(False, False)
        
        largura = 300
        altura = 250
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = ((altura_tela - altura) // 2) - 50
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        
        self.create_widgets()
        self.deiconify()
        
    def create_widgets(self):
        style = ttk.Style()

        style.configure("Formulario.TLabel", font=("Segoe UI", 12))       
        nome_lbl = ttk.Label(self, text="Nome:", style="Formulario.TLabel")
        nome_lbl.place(x=30, y=20)
        
        style.configure("Formulario.TEntry", font=("Segoe UI", 20),  padding=5)
        nome_ety = ttk.Entry(self, width=35, style="Formulario.TEntry")
        nome_ety.place(x=30, y=50)
        
        turma_lbl = ttk.Label(self, text="Turma:", style="Formulario.TLabel")
        turma_lbl.place(x=30, y=105)
        turma_var = tk.StringVar()
        turma_cbb = ttk.Combobox(self, textvariable=turma_var)
        turma_cbb['values'] = ('18:30 - 19:30', '20:00 - 21:30')
        turma_cbb.place(x=110, y=110)
        
        style.configure("Formulario.TButton", font=("Segoe Ui SemiBold", 14), padding=4)
        cdt_btn = ttk.Button(self, text="Cadastrar", style="Formulario.TButton",
                     command=lambda: self.cadastrar(nome_ety.get(), turma_cbb.get()))
        cdt_btn.place(x=80, y=175)
        
    def cadastrar(self, nome, turma):
        if not nome or not turma:
            messagebox.showerror("Erro", "Campo em Branco, verifique as informações!")
        else:
            aluno = Aluno(nome, turma)
            cad_aluno(aluno)
            if self.atualizar_atrasados:
                self.atualizar_atrasados()
            self.destroy()