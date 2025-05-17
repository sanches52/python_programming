print('\n <<<< AULA 18 >>>> \n')

##############################################################
# >>>>>> BIBLIOTECA TKINTER <<<<<<
############################################################## 

import tkinter as tk

def mostrar():
    mostrar_nome = entry_nome.get()
    mostrar_texto.config(text = mostrar_nome)

janela =  tk.Tk()
janela.title('Teste TKinter')
janela.geometry('500x500')

nome = tk.Label(janela,text = 'Nome')
nome.pack(pady=10)

entry_nome = tk.Entry(janela)
entry_nome.pack(pady=10)

botao = tk.Button(janela, text='clique aqui',command=mostrar)
botao.pack(pady=10)

mostrar_texto = tk.Label(janela, text = '')
mostrar_texto.pack(pady=10)

janela.mainloop()
