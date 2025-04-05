# EXERCÍCIOS

print('\n <<<< EXERCÍCIOS >>>> \n')

# **Ex. 1:** Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000.

# i = 0
# while i <= 1000:
#     print(i) 
#     i = i + 1

# **Ex. 2:** Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

i = 0
lista_nomes = []
while i <= 10:
    nome = input('Digite seu nome: ')
    lista_nomes += [nome]
    i += 1
    # print(lista_nomes)

print(lista_nomes)