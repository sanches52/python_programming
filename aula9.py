print('\n <<<< AULA 9 >>>> \n')

##############################################################
# >>>>>> ESTRUTURA DE REPETIÇÃO (LOOPS) <<<<<<
##############################################################

##############################################################
# >>>>>> FOR <<<<<<

# Não são infinitas!
##############################################################

# SINTAXE

# for variavel in sequencia:
#     faca_isso

# for numero in range(1,11):
#     print(numero)

# for numero in range(3):
#     nome = input('Digite seu nome: ')
#     idade = int(input(('Digite sua idade: ')))
#     print(f'{nome} , {idade}')

import random

lista  = [3,2,1]
for chances in lista:
    aleatorio =  random.randint(1,2)
    chute = int(input('Escolha um numero: '))  
    if aleatorio == chute:
        print('Ganhou Jogo o número é', aleatorio)
        break
    else:       
        
        print('Errou Feio número foi, ', aleatorio)
        print('Você tem', chances-1, 'chances')  
else:
    print('Suas chances se esgotaram', chances)   

##############################################################
# >>>>>> WHILE <<<<<<

# São infinitas!
##############################################################

# SINTAXE
# c = 10
# while c > 0:
#     print(c) 
#     c = c - 1

# c = 0
# while c <=0:
#     print(c) 
#     c = c + 1

import random

chances = 3
while chances > 0 :
    aleatorio =  random.randint(1,20)
    chute = int(input('Escolha um numero: '))  
    if aleatorio == chute:
        print('Ganhou Jogo o número é', aleatorio)
        break
    else:       
        chances = chances - 1
        print('Errou Feio número foi, ', aleatorio)
        print(f'Você tem, {chances}, chances')  
else:
    print('Suas chances se esgotaram', chances) 