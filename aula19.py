print('\n <<<< AULA 19 >>>> \n')

##############################################################
# >>>>>> BIBLIOTECA  - SQLITE3 <<<<<<
############################################################## 

# O SQLite3 é um sistema de gerenciamento de banco de dados relacional (RDBMS) leve, rápido e 
# embutido em uma biblioteca que pode ser usada diretamente em aplicativos. 

# FUNÇÕES CRUD:
    # CREATE
    # READ
    # UPDATE
    # DELETE

import sqlite3
import tkinter as tk
from tkinter import Listbox, messagebox

def create_db():

    # Conectar ao banco de dados (se o banco não existir, ele será criado)
    conn = sqlite3.connect('my_database.db')

    # Cursor para interagir com o banco de dados
    cursor = conn.cursor()

    # Criando a  tabela
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS pessoas (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            peso REAL NOT NULL,
                            altura REAL NOT NULL,
                            imc REAL NOT NULL
                    )''')

    # Salvar as mudanças
    conn.commit()

    # fechar a conexão
    conn.close()


def calc_imc(peso, altura):
    if altura > 0:
            return round(peso / (altura ** 2), 2)
    return None


def validar_dados():
    if not entry_nome.get() or entry_peso.get() or entry_altura.get():
        messagebox.showerror('Erro', 'Digite os dados!')
        return False
    
    if not entry_peso.get().replace('.','',1).isdigit() or not entry_altura.get().replace('.','',1).isdigit():
        messagebox.showerror('Erro', 'Peso e altura devem ser valores corretos!')
        return False
    return True


def adicionar():

    if validar_dados():
    nome = entry_nome.get()
    peso = entry_peso.get()
    altura = entry_altura.get()

    imc = calc_imc(peso,altura)

    if imc is not None:

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO pessoas (nome, peso, altura, imc) VALUES(?,?,?,?)",
                        (nome, peso, altura, imc))

        conn.commit()
        conn.close()

        messagebox.showinfo('Dados', 'Dados inseridos com sucesso!')

    #LIMPA LISTA
    
    else:
        messagebox.showerror('Erro', 'Não é possivel inserir!')
    

def listar():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pessoas")
    registros = cursor.fetchall()

    conn.close()

    Listbox.delete(0,tk.END)

    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, IMC: {registro[4]}")


def buscar():

    id = entry_id.get()
    if id.isdigit():

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pessoas WHERE id = ?", (id))
        pessoa = cursor.fetchone()
        
        conn.close()

        if pessoa:
            entry_nome.delete(0,tk.END)
            entry_nome.insert(tk.END, pessoa[1])
            entry_peso.delete(0,tk.END)
            entry_peso.insert(tk.END, pessoa[2])
            entry_altura.delete(0,tk.END)
            entry_altura.insert(tk.END, pessoa[3])

        else:
            messagebox.showerror('Atenção', 'Pessoa não encontrada!')

    else:
        messagebox.showerror('Erro', 'Contém erros!')


def atualizar():
    if entry_id.get().isdigit() and validar_dados():
        id = int(entry_id.get())
        nome = int(entry_nome.get())
        peso = int(entry_peso.get())
        altura = int(entry_altura.get())

        imc = calc_imc(peso, altura)

        if imc is not None:

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE pessoas SET nome=?, peso=?, altura=?, imc=?",
                        (nome, peso, altura, imc))

        conn.commit()
        conn.close()

        messagebox.showinfo('Dados', 'Dados inseridos com sucesso!')

    #LIMPA LISTA
    
    else:
        messagebox.showerror('Erro', 'Não é possivel inserir!')


def excluir():

    id = int(entry_id.get())
    if id.isdigit():

        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        cursor.execute("DELETE * FROM pessoas WHERE id = ?", (id))

        conn.commit()
        conn.close()

        messagebox.showinfo('Atenção', 'Dados deletados com sucesso!')

    else:
        messagebox.showerror('Erro', 'Algo deu errado!')
    

def limpar():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)





# -------------- CONSULTAR DADOS NO BANCO DE DADOS -------------------

# # Consultar os dados na tabelinha
# cursor.execute('SELECT * FROM clientes')

# # Com um loop acessar os resultados
# for row in cursor.fetchall():
#     print(row)


# -------------- ADICIONAR DADOS AO BANCO DE DADOS -------------------

# # Inserir alguns dados na tabela
# cursor.execute('''
# INSERT INTO clientes (nome, idade) VALUES ('João', 30)
# ''')
# cursor.execute('''
# INSERT INTO clientes (nome, idade) VALUES ('Maria', 25)
# ''')

# -------------- ATUALIZAR DADOS NO BANCO DE DADOS -------------------

# # Atualizar a idade para 31 anos
# cursor.execute('''
# UPDATE clientes SET idade = 31 WHERE nome = 'João'
# ''')

# -------------- MODIFICAR BANCO DE DADOS -------------------

# cursor.execute('''
# ALTER TABLE clientes ADD COLUMN email TEXT
# ''')