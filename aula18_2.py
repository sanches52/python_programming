print('\n <<<< AULA 18 >>>> \n')

##############################################################
# >>>>>> BIBLIOTECA  - CALCULADORA <<<<<<
############################################################## 

import tkinter as tk

# -------------- FUNÇÕES ---------------
def soma():
    numero1 = float(entry_n1.get())
    numero2 = float(entry_n2.get())
    s = numero1 + numero2
    mostrar_r.config(text=s)

def subtracao():
    numero1 = float(entry_n1.get())
    numero2 = float(entry_n2.get())
    s = numero1 - numero2
    mostrar_r.config(text=s)

def multiplicacao():
    numero1 = float(entry_n1.get())
    numero2 = float(entry_n2.get())
    s = numero1 * numero2
    mostrar_r.config(text=s)

def div():
    numero1 = float(entry_n1.get())
    numero2 = float(entry_n2.get())
    s = numero1 / numero2
    mostrar_r.config(text=s)


root = tk.Tk()
root.title('CALCULADORA')
root.geometry('400x200')

# -------------- INPUT ---------------
n1 = tk.Label(root,text = 'numero 1', font='arial')
n1.grid(row=0, column=0, pady=5, padx=10)

entry_n1 = tk.Entry(root, width= 10)
entry_n1.grid(row=0, column=1, pady=5)

n2 = tk.Label(root,text = 'numero 2', font='arial')
n2.grid(row=1, column=0, pady=5, padx=10)

entry_n2 = tk.Entry(root, width= 10)
entry_n2.grid(row=1, column=1, pady=5, padx=5)

# -------------- BOTÕES ---------------

btn_soma = tk.Button(root, text='soma', command=soma)
btn_soma.grid(row =4, column=0, pady=5, padx=5)

btn_sub = tk.Button(root, text='Subtração', command=subtracao)
btn_sub.grid(row =4, column=1, pady=5, padx=5)

btn_mult = tk.Button(root, text='Multiplicação',command=multiplicacao)
btn_mult.grid(row =4, column=2, pady=5, padx=5)

btn_div = tk.Button(root, text='Divisão', padx=5, command=div)
btn_div.grid(row =4, column=3, pady=5, padx=5)

# -------------- OUTPUT ---------------

mostrar_r = tk.Label(root, text = '=', font='arial')
mostrar_r.grid(row=5,column=1)


root.mainloop()