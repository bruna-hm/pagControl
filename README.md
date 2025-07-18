##pagControl

pagControl é um aplicativo desktop desenvolvido em Python com foco em estudos e para atender a uma necessidade real de controle de pagamentos de alunos. O projeto me permitiu aplicar conceitos de Programação Orientada a Objetos (OOP) e aprofundar conhecimentos com a linguagem.

<br>Tecnologias:
- Python
- Tkinter
- PyInstaller

<br>Funcionalidades:
- Cadastro de alunos
- Registro de pagamentos
- Visualização de alunos e seus pagamentos
- Edição de turma e valor de pagamento
- Exclusão de alunos (e seus respectivos pagamentos)

## Como Usar
1. Clone o repositório:  
   ```bash
   git clone https://github.com/bruna-hm/pagControl.git
   ```
   
2. Acesse o diretório do projeto:  
   ```bash
   cd pagControl
   ```

3. Crie e ative o ambiente virtual (no Windows):  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Instale as dependências do projeto:  
   ```bash
   pip install -r requirements.txt
   ```

5. Gere o executável com o PyInstaller:  
   ```bash
   pyinstaller main.spec
   ```

6. Após a finalização, entre na pasta `dist`:  
   ```bash
   cd dist
   ```

7. Dentro da pasta `dist`, localize o executável gerado e crie um atalho para ele na área de trabalho, se desejar.

## Sugestões e contribuições
Qualquer melhoria ou comentário sobre o projeto, por favor, entrem em contato por: 
<strong>brunaahm@gmail.com</strong>