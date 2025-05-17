import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para criar/conectar ao banco de dados e criar a tabela se não existir
def create_db():
    conn = sqlite3.connect('crud_database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        peso REAL NOT NULL,
                        altura REAL NOT NULL,
                        imc REAL NOT NULL)''')
    conn.commit()
    conn.close()

# Função para calcular o IMC
def calcular_imc(peso, altura):
    if altura > 0:
        return round(peso / (altura ** 2), 2)
    return None

# Função para validar os campos
def validar_campos():
    if not entry_nome.get() or not entry_peso.get() or not entry_altura.get():
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return False
    
    if not entry_peso.get().replace('.', '', 1).isdigit() or not entry_altura.get().replace('.', '', 1).isdigit():
        messagebox.showerror("Erro", "Peso e altura devem ser números válidos.")
        return False
    
    return True

# Função para adicionar um novo registro
def adicionar():
    if validar_campos():
        nome = entry_nome.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = calcular_imc(peso, altura)

        if imc is not None:
            conn = sqlite3.connect('crud_database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pessoas (nome, peso, altura, imc) VALUES (?, ?, ?, ?)",
                           (nome, peso, altura, imc))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", f"Registro adicionado!\nIMC: {imc}")
            limpar_campos()
            listar()
        else:
            messagebox.showerror("Erro", "Altura inválida.")

# Função para listar os registros no banco de dados
def listar():
    conn = sqlite3.connect('crud_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoas")
    registros = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)  # Limpar lista antes de listar novamente
    for registro in registros:
        listbox.insert(tk.END, f"ID: {registro[0]}, Nome: {registro[1]}, IMC: {registro[4]}")

# Função para buscar dados pelo ID e preencher os campos para edição
def buscar():
    id = entry_id.get()

    if id.isdigit():
        conn = sqlite3.connect('crud_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pessoas WHERE id = ?", (id,))
        pessoa = cursor.fetchone()
        conn.close()

        if pessoa:
            entry_nome.delete(0, tk.END)
            entry_nome.insert(tk.END, pessoa[1])
            entry_peso.delete(0, tk.END)
            entry_peso.insert(tk.END, pessoa[2])
            entry_altura.delete(0, tk.END)
            entry_altura.insert(tk.END, pessoa[3])
        else:
            messagebox.showwarning("Atenção", "Pessoa não encontrada.")
    else:
        messagebox.showerror("Erro", "ID deve ser um número.")

# Função para atualizar um registro
def atualizar():
    if entry_id.get().isdigit() and validar_campos():
        id = int(entry_id.get())
        nome = entry_nome.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = calcular_imc(peso, altura)

        if imc is not None:
            conn = sqlite3.connect('crud_database.db')
            cursor = conn.cursor()
            cursor.execute("UPDATE pessoas SET nome = ?, peso = ?, altura = ?, imc = ? WHERE id = ?",
                           (nome, peso, altura, imc, id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Registro atualizado!")
            limpar_campos()
            listar()
        else:
            messagebox.showerror("Erro", "Altura inválida.")
    else:
        messagebox.showerror("Erro", "ID inválido ou campos não preenchidos corretamente.")

# Função para excluir um registro
def excluir():
    id = entry_id.get()
    
    if id.isdigit():
        conn = sqlite3.connect('crud_database.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Registro excluído!")
        limpar_campos()
        listar()
    else:
        messagebox.showerror("Erro", "ID deve ser um número.")

# Função para limpar os campos de entrada
def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)

# Interface gráfica
root = tk.Tk()
root.title("CRUD Básico - IMC")

# Criando um Frame para organizar os widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Labels e entradas dentro do frame
tk.Label(frame, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Nome:").grid(row=1, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Peso (kg):").grid(row=2, column=0, padx=5, pady=5)
entry_peso = tk.Entry(frame)
entry_peso.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Altura (m):").grid(row=3, column=0, padx=5, pady=5)
entry_altura = tk.Entry(frame)
entry_altura.grid(row=3, column=1, padx=5, pady=5)

# Listbox para exibir registros
listbox = tk.Listbox(frame, width=50, height=10)
listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Botões dentro do frame
btn_adicionar = tk.Button(frame, text="Adicionar", command=adicionar)
btn_adicionar.grid(row=4, column=0, padx=5, pady=5)

btn_buscar = tk.Button(frame, text="Buscar", command=buscar)
btn_buscar.grid(row=4, column=1, padx=5, pady=5)

btn_atualizar = tk.Button(frame, text="Atualizar", command=atualizar)
btn_atualizar.grid(row=5, column=0, padx=5, pady=5)

btn_excluir = tk.Button(frame, text="Excluir", command=excluir)
btn_excluir.grid(row=5, column=1, padx=5, pady=5)

# Inicializa o banco de dados
create_db()
listar()

# Inicia o loop principal do Tkinter
root.mainloop()
