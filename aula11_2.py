print('\n <<<< EXERCÍCIOS >>>> \n')

# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    numero =  int(input('Insira um número: '))
except TypeError:
    print('Você inseriu um tipo de dado incorreto')
except ValueError:
    print('Você inseriu um tipo de dado incorreto')
else:
   print(numero)

# # def verificar():
# #     try:
# #        numero  =  int(input('>>'))
# #        print(numero - 1)
# #     except ValueError as erro:
# #        print(erro) 
# #     finally:
# #         print('Fim do carregamento!')

# # verificar()   

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

import random

chances = 3

while  chances > 0:
   chances = chances - 1
   n  =   int(input('Digite um numero> '))
   r = random.randint(1,2)

   if n  == r : 
      print(f'vc ganhou o jogo, o número é: {r}') 
      break
   else: 
      print(f'Voc perdeu o jogo, o número é {r}')     

   try:
    n1 =  int(input('Insira o numero 1: '))
    n2 =  int(input('Insira o numero 2: '))
    div  =  n1 / n2
    print(div)
   except ZeroDivisionError:
    print('O divisor não pode ser 0')
   except ValueError:
    print('O Precisa ser um número')

# def verificar2():
#     try:
#        numero2  =  int(input('>>'))
#        numero3  =  int(input('>>'))
#        result  = numero2/numero3

#     except ValueError as erro:
#        print(erro) 
#     except ZeroDivisionError as erro:
#        print(erro)  
#     else: 
#        print(result)     
#     finally:
#         print('Fim do carregamento!')

# verificar2()  

# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o parameter elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

def mostrar_indice(number):
    lista = [1,2,3,4,5,6]
    
    try:
        print(lista[number])
    except IndexError:
       print('Esse indice não existe')


number  =  int(input('Digite o valor do indice'))   
mostrar_indice(number)   

# def handle(lista):
#     try: 
#         n = int(input(':'))
#         i = lista[n]
#     except ValueError:
#         print('Utilize números apenas!')    
#     except IndexError:
#         print('Esse indice não existe na lista!', n)
#     else: 
#         print(f'Essa é a lista: {lista}, e esse é o valor {i}, indice é o {n}')



# lista =  [1,4,6,56,6,56,65]
# handle(lista)

# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

def div():
    try:
       n  = int(input())
       n1  = int(input()) 
       print('Divisão >   ', n / n1)
    except ZeroDivisionError: 
      print('Não pode dividir por zero')

div()

# def verificar3():
#     try:
#        numero2  =  int(input('>>'))
#        numero3  =  int(input('>>'))
#        result  = numero2/numero3
#        print(result)

#     except ZeroDivisionError:
#        print('O divisor não pode ser zero!')  
   


# verificar3()