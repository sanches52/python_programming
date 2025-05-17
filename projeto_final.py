import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Conectar ao banco de dados
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    endereco TEXT
)
""")
conn.commit()

# Funções
def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    if nome:
        cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)", (nome, email, telefone, endereco))
        conn.commit()
        listar()
        limpar_campos()
    else:
        messagebox.showwarning("Atenção", "Nome é obrigatório.")

def listar():
    for i in tree.get_children():
        tree.delete(i)
    cursor.execute("SELECT * FROM clientes")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

def excluir():
    item = tree.selection()
    if item:
        cliente_id = tree.item(item)["values"][0]
        cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
        conn.commit()
        listar()
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para excluir.")

def editar():
    item = tree.selection()
    if item:
        global cliente_id_editar
        cliente_id_editar = tree.item(item)["values"][0]
        nome, email, telefone, endereco = tree.item(item)["values"][1:]
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_nome.insert(0, nome)
        entry_email.insert(0, email)
        entry_telefone.insert(0, telefone)
        entry_endereco.insert(0, endereco)
    else:
        messagebox.showwarning("Atenção", "Selecione um cliente para editar.")

def salvar_edicao():
    try:
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        endereco = entry_endereco.get()
        cursor.execute("UPDATE clientes SET nome=?, email=?, telefone=?, endereco=? WHERE id=?",
                       (nome, email, telefone, endereco, cliente_id_editar))
        conn.commit()
        listar()
        limpar_campos()
    except:
        messagebox.showinfo("Erro", "Nenhum cliente selecionado para editar.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)

# Interface
root = tk.Tk()
root.title("Cadastro de Clientes")

tk.Label(root, text="Nome").grid(row=0, column=0)
tk.Label(root, text="Email").grid(row=1, column=0)
tk.Label(root, text="Telefone").grid(row=2, column=0)
tk.Label(root, text="Endereço").grid(row=3, column=0)

entry_nome = tk.Entry(root)
entry_email = tk.Entry(root)
entry_telefone = tk.Entry(root)
entry_endereco = tk.Entry(root)

entry_nome.grid(row=0, column=1)
entry_email.grid(row=1, column=1)
entry_telefone.grid(row=2, column=1)
entry_endereco.grid(row=3, column=1)

tk.Button(root, text="Cadastrar", command=cadastrar).grid(row=4, column=0)
tk.Button(root, text="Editar", command=editar).grid(row=4, column=1)
tk.Button(root, text="Salvar Edição", command=salvar_edicao).grid(row=4, column=2)
tk.Button(root, text="Excluir", command=excluir).grid(row=4, column=3)

cols = ("ID", "Nome", "Email", "Telefone", "Endereço")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
tree.grid(row=5, column=0, columnspan=4)

listar()

root.mainloop()
