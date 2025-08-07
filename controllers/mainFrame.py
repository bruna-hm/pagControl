import tkinter as tk
from tkinter import ttk
import datetime as dt
from controllers.cadastroFrame import cadastroFrame
from controllers.pagamentosFrame import pagamentoFrame
from controllers.alunosFrame import alunosFrame
from views.utils import mes_atual, mes_pt, dia_semana, resource_path
from dao.pagDao import atrasados 

class mainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(default=resource_path("assets/img/dojo.ico"))
        self.title("Kanshin Dojo - Sistema de Alunos")
        self.configure(bg="white")  
        self.resizable(False, False)
        
        largura = 800
        altura = 500
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = ((altura_tela - altura) // 2) - 50
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        
        self.atrasados_labels = []
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        
        style.configure("Titulo.TLabel", font=("Bahnschrift SemiBold Condensed", 18))
        style.configure("Subtitulo.TLabel", font=("Bahnschrift Light", 12))
        style.configure("Data.TLabel", font=("Bahnschrift SemiBold", 16))

        infos_lbl = ttk.Label(self, text="Bujinkan Kanshin Dojo", style="Titulo.TLabel", background="white")
        infos_lbl.place(x=155, y=35)

        infos2_lbl = ttk.Label(self, text="Sensei João Francisco", style="Subtitulo.TLabel", background="white")
        infos2_lbl.place(x=165, y=65)

        logo_path = resource_path("assets/img/logo.png")
        self.img = tk.PhotoImage(file=logo_path)
        img_lbl = ttk.Label(self, image=self.img, background="white")
        img_lbl.place(x=30, y=40)

        date = dt.datetime.now()
        mes = mes_atual()
        dia_da_semana = dia_semana(date.weekday())
        date_lbl = ttk.Label(self, 
                            text=f"   {dia_da_semana}\n {date.strftime('%d')}/{mes_pt(mes)}/{date.strftime('%Y')}",
                            style="Data.TLabel", background="white")
        date_lbl.place(x=180, y=105)
        
        style.configure("Style.TButton", font=("Segoe UI", 10), padding=(5, 2))
        
        cadastro_btn = ttk.Button(self, text="Cadastrar Aluno", style="Style.TButton", command=self.abrir_aluno)
        cadastro_btn.place(x=500, y=25, width=200)
        registro_btn = ttk.Button(self, text="Registrar pagamento", style="Style.TButton", command=self.abrir_pagamento)
        registro_btn.place(x=500, y=65, width=200)
        visualizar_alunos = ttk.Button(self, text="Visualizar Pagamentos", style="Style.TButton", command=self.abrir_alunos)
        visualizar_alunos.place(x=500, y=105, width=200)
        
        sep = ttk.Separator(self, orient="horizontal")
        sep.place(relx=0, rely=0.4, relwidth=1, relheight=5)

        self.atrasados_frame = tk.Frame(self, bg="#ffd9df", bd=1, relief="solid")
        self.atrasados_frame.place(relx=0.01, rely=0.41, relwidth=0.98, relheight=0.58)
        self.popular_atrasados()

    def popular_atrasados(self):
        if hasattr(self, 'atrasados_labels'):
            for lbl in self.atrasados_labels:
                lbl.destroy()
        
        self.atrasados_labels = []
        mes = mes_atual()
        pgt_atrasado = atrasados()
        
        style = ttk.Style()
        style.configure("Titulo.TLabel", font=("Segoe UI Semibold", 14))
        atrasados_lbl = ttk.Label(self, text=f"* Pagamentos atrasados de {mes_pt(mes)} *", style="Titulo.TLabel", background="#ffd9df")
        atrasados_lbl.place(relx=0.3, y=210)
        self.atrasados_labels.append(atrasados_lbl)
            
        for i in range(len(pgt_atrasado)):
            atrasado_lbl = tk.Label(self, text=f"◉ {pgt_atrasado[i][1]}", font=("Segoe Ui", 12), background="#ffd9df")
            atrasado_lbl.place(x=300, y=250 + (i * 30))
            self.atrasados_labels.append(atrasado_lbl)
        
    def abrir_aluno(self):
        aluno_form = cadastroFrame(self, atualizar_atrasados=self.popular_atrasados)
        aluno_form.grab_set()
        
    def abrir_pagamento(self):
        pagamento_form = pagamentoFrame(self, atualizar_atrasados=self.popular_atrasados)
        pagamento_form.grab_set()
        
    def abrir_alunos(self):
        alunos_view = alunosFrame(self, atualizar_atrasados=self.popular_atrasados)
        alunos_view.grab_set()