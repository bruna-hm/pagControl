import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from views.utils import mes_pt, meses_pt, resource_path
from dao.alunoDao import listar_alunos, cbb_alunos, anos, edit_aluno, del_aluno, id_aluno
from dao.pagDao import listar_pgts, edit_pgt, meses_pgt, anos_pgt

class alunosFrame(tk.Toplevel):
    def __init__(self, master=None, atualizar_atrasados=None):
        super().__init__(master)
        self.iconbitmap(default=resource_path("assets/img/dojo.ico"))
        self.atualizar_atrasados = atualizar_atrasados
        self.title("Visualização de Alunos")
        self.configure(bg="white")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()
        self.focus_force()
        
        largura = 900
        altura = 600
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        pos_x = (largura_tela - largura) // 2
        pos_y = ((altura_tela - altura) // 2) - 50
        self.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.create_widgets()
        
    def create_widgets(self):
        style = ttk.Style()
        
        style.configure("Treeview",
        font=("Segoe UI", 12),
        background="#eaeaea",
        fieldbackground="white",
        foreground="black")

        style.configure("Treeview.Heading",
        font=("Segoe UI", 14, "bold"))
        
        container = tk.Frame(self)
        container.place(x=15, y=15, width=600, relheight=0.95)

        scrollbar = ttk.Scrollbar(container, orient='vertical')
        scrollbar.pack(side='left', fill='y')

        self.alunos_tree = ttk.Treeview(container, yscrollcommand=scrollbar.set)
        self.alunos_tree.pack(side='left', fill='both', expand=True)
        self.alunos_tree.heading('#0', text='Alunos e Pagamentos')

        scrollbar.config(command=self.alunos_tree.yview)

        self.popular_treeview()

        style.configure("Acao.TButton", font=("Consolas", 12), padding=(10, 5))
        editTurma_btn = ttk.Button(self, text="Editar Turma", style="Acao.TButton",
                           command=lambda: self.abrir_container_editurma())
        editTurma_btn.place(x=660, y=40, width=200)

        editValor_btn = ttk.Button(self, text="Editar Valor", style="Acao.TButton",
                           command=lambda: self.abrir_container_edivalor())
        editValor_btn.place(x=660, y=80, width=200)

        delAluno_btn = ttk.Button(self, text="Excluir Aluno", style="Acao.TButton",
                          command=lambda: self.abrir_container_delAluno())
        delAluno_btn.place(x=660, y=120, width=200)

    def popular_treeview(self):
        for item in self.alunos_tree.get_children():
            self.alunos_tree.delete(item)
        
        aluno_ids = {}
        alunos = listar_alunos()
        for n in alunos:
            nome = n[1]
            turma = n[2]
            item_id = self.alunos_tree.insert('', 'end', text=f"‣ {nome} - {turma}", open=False)
            aluno_ids[nome] = item_id
        
        ano_ids_por_aluno = {}
        pgts = listar_pgts()
        for p in pgts:
            aluno_id = p[0]
            mes = p[1]
            ano = p[2]
            valor = p[3]

            for a in alunos:
                if aluno_id == a[0]:
                    nome = a[1]
                    parent_id = aluno_ids.get(nome)
                    if parent_id:
                        chave = (nome, ano)
                        if chave not in ano_ids_por_aluno:
                            ano_id = self.alunos_tree.insert(parent_id, 'end', text=str(ano), open=False)
                            ano_ids_por_aluno[chave] = ano_id
                        else:
                            ano_id = ano_ids_por_aluno[chave]

                        self.alunos_tree.insert(ano_id, 'end', text=f"{mes_pt(mes)} : R$ {valor}", open=False)
    
    def abrir_container_editurma(self):
        style = ttk.Style()
        style.configure("Main.TFrame", background="white")
        self.container_edit = ttk.Frame(self, style="Main.TFrame")
        self.container_edit.place(x=650, y=220, width=225, height=180)
        self.configure(bg="white")
        
        nome_lbl = tk.Label(self.container_edit, text="Nome:", font=("Consolas", 12), background="white")
        nome_lbl.place(x=10, y=10)
        nome_cbb = ttk.Combobox(self.container_edit, width=30)
        nome_cbb['values'] = [nome for nome in cbb_alunos()]
        nome_cbb.place(x=10, y=35)
        
        turma_lbl = tk.Label(self.container_edit, text="Nova Turma:", font=("Consolas", 12), background="white")
        turma_lbl.place(x=10, y=60)
        turma_cbb = ttk.Combobox(self.container_edit, width=30)
        turma_cbb['values'] = ('18:30 - 19:30', '20:00 - 21:30')
        turma_cbb.place(x=10, y=85)
        
        style = ttk.Style()
        style.configure("Formulario.TButton", font=("Consolas", 10), padding=5)

        salvar_btn = ttk.Button(self.container_edit, text="Salvar", style="Formulario.TButton",
                                command=lambda: ((
                                    edit_aluno(turma_cbb.get(), id_aluno(nome_cbb.get())), 
                                    self.popular_treeview(),
                                    self.atualizar_atrasados(),
                                    self.container_edit.destroy())
                                    if turma_cbb.get() and nome_cbb.get() else messagebox.showerror("Erro", "Campo em Branco, verifique as informações!")
                                ))
        salvar_btn.place(x=10, y=130)

        cancel_btn = ttk.Button(self.container_edit, text="Cancelar", style="Formulario.TButton",
                                command=self.container_edit.destroy)
        cancel_btn.place(x=120, y=130)
        
    def abrir_container_edivalor(self):
        style = ttk.Style()
        style.configure("Main.TFrame", background="white")
        self.container_edit = ttk.Frame(self, style="Main.TFrame")
        self.container_edit.place(x=650, y=220, width=225, height=240)
        
        nome_lbl = tk.Label(self.container_edit, text="Nome:", font=("Consolas", 12), background="white")
        nome_lbl.place(x=30, y=10)
        nome_cbb = ttk.Combobox(self.container_edit, width=20)
        nome_cbb['values'] = [nome for nome in cbb_alunos()]
        nome_cbb.place(x=30, y=35)
        
        anomes_lbl = tk.Label(self.container_edit, text="Ano e Mês", font=("Consolas", 12), background="white")
        anomes_lbl.place(x=30, y=60)
        
        ano_cbb = ttk.Combobox(self.container_edit, width=5)
        ano_cbb.place(x=30, y=85)
        mes_cbb = ttk.Combobox(self.container_edit, width=8)
        mes_cbb.place(x=90, y=85)
        
        valor_lbl = tk.Label(self.container_edit, text="Novo Valor:", font=("Consolas", 12), background="white")
        valor_lbl.place(x=30, y=110)
        valor_ety = tk.Entry(self.container_edit, width=23)
        valor_ety.place(x=30, y=140)
        
        style = ttk.Style()
        style.configure("Formulario.TButton", font=("Consolas", 10), padding=5)

        salvar_btn = ttk.Button(
            self.container_edit,
            text="Salvar",
            style="Formulario.TButton",
            command=lambda: (
                (edit_pgt(float(valor_ety.get()), id_aluno(nome_cbb.get()), mes_cbb.get(), int(ano_cbb.get())),
                 self.popular_treeview(),
                self.container_edit.destroy()) 
                if valor_ety.get() and nome_cbb.get() and mes_cbb.get() and ano_cbb.get() 
                else messagebox.showerror("Erro", "Campo em Branco, verifique as informações!")
            )
        )
        salvar_btn.place(x=10, y=180)


        cancel_btn = ttk.Button(
            self.container_edit,
            text="Cancelar",
            style="Formulario.TButton",
            command=self.container_edit.destroy
        )
        cancel_btn.place(x=110, y=180)
        
        def atualizar_anos(event):
            nome = nome_cbb.get()
            if nome:
                aluno_id = id_aluno(nome)
                anos_disponiveis = anos_pgt(aluno_id)
                ano_cbb['values'] = anos_disponiveis
        
        def atualizar_meses(event):
            nome = nome_cbb.get()
            if nome:
                aluno_id = id_aluno(nome)
                meses_disponiveis = meses_pgt(aluno_id)
                meses = meses_pt(meses_disponiveis)
                mes_cbb['values'] = meses
        
        nome_cbb.bind("<<ComboboxSelected>>", atualizar_anos)
        ano_cbb.bind("<<ComboboxSelected>>", atualizar_meses)        
            
    def abrir_container_delAluno(self):
        style = ttk.Style()
        style.configure("Main.TFrame", background="white")
        self.container_delAluno = ttk.Frame(self, style="Main.TFrame")
        self.container_delAluno.place(x=650, y=220, width=225, height=120)
        
        nome_lbl = tk.Label(self.container_delAluno, text="Aluno:", font=("Consolas", 12), background="white")
        nome_lbl.place(x=10, y=10)
        nome_cbb = ttk.Combobox(self.container_delAluno, width=29)
        nome_cbb['values'] = [nome[0] for nome in cbb_alunos()]
        nome_cbb.place(x=10, y=35)
        
        style = ttk.Style()
        style.configure("Formulario.TButton", font=("Consolas", 10), padding=5)

        excluir_btn = ttk.Button(
            self.container_delAluno,
            text="Excluir",
            style="Formulario.TButton",
            command=lambda: ((
                del_aluno(id_aluno(nome_cbb.get())),
                self.popular_treeview(),
                self.atualizar_atrasados(),
                self.container_delAluno.destroy())
                if nome_cbb.get() 
                else messagebox.showerror("Erro", "Campo em Branco, verifique as informações!"),
            )
        )
        excluir_btn.place(x=10, y=70)

        cancel_btn = ttk.Button(
            self.container_delAluno,
            text="Cancelar",
            style="Formulario.TButton",
            command=self.container_delAluno.destroy
        )
        cancel_btn.place(x=110, y=70)