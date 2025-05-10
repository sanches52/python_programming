print('\n <<<< AULA 14 >>>> \n')

##############################################################
# >>>>>> MATCH CASES <<<<<<
############################################################## 

# Semelhante as condicionais, é conhecido também como Structural Pattern Matching, faz o computador fazer escolhas de forma simplificada e objetiva. 
# FAZ APENAS COMPARAÇÕES NAS ESCOLHAS.
# if-elif-else é recomendado para lógicas mais robustas e complexas.

# import timeit  #precisa ter a biblioteca instalada no pc para funcionar


# --------------- ESTRUTURA COM IF-ELIF-ELSE --------------

print('\n <<<< Exemplo 1 - if-elif-else >>>> \n')
n = 10
if n == 0:
   print("zero")
else:
   print('Menor ou maior')

print('\n <<<< Exemplo 2 - if-elif-else >>>> \n')

def check_type_with_if(value):
    if isinstance(value, str):
        print("É uma string")
    elif isinstance(value, int):
        print("É um inteiro")
    elif isinstance(value, float):
        print("É um número de ponto flutuante")
    else:
        print("Tipo não reconhecido")

check_type_with_if("Olá")   # Saída: É uma string
check_type_with_if(42)      # Saída: É um inteiro
check_type_with_if(3.14)    # Saída: É um número de ponto flutuante

# def teste2():
#     escolha  =  'z'

#     if escolha == 'z':
#         print('Acertou ')
#     else:
#         print('errou') 

# time = timeit.timeit(teste2, number=10)
# print('função2', time)

# --------------- ESTRUTURA COM MATCH-CASE --------------

print('\n <<<< Exemplo 1 - match-case >>>> \n')

n = 0
match n:
    case 0:
        print("é zero")
    case 1:
        print("Menor ou maior")
    case 2:
        print('É dois...')
    case _:
        print('Algo desconhecido')   

print('\n <<<< Exemplo 2 - match-case >>>> \n') 

a  = 20
b  = 30
match a,b:
    case 0:
        print('É zero')
    case 20:
        print('é 20')
    case _:
         print('Não é nada')

# a  = int(input())
# b  = int(input())
# match a,b:
#     case 0 , 1:
#         print('Acesso ok')
#     case _:
#         print('Tente novamente')

print('\n <<<< Exemplo 3 - match-case >>>> \n')

def check_type_with_match(value):
    match value:
        case str():
            print("É uma string")
        case int():
            print("É um inteiro")
        case float():
            print("É um número de ponto flutuante")
        case bool():
            print("É um número de boleano")   
        case _:
            print("Desconhecido")

check_type_with_match("Olá")  # Saída: É uma string
check_type_with_match(42)     # Saída: É um inteiro
check_type_with_match(3.14)   # Saída: É um número de ponto flutuante

print('\n <<<< Exemplo 4 - match-case >>>> \n')

num = int(input('Insira aqui um número: '))

match num:
    case 0:
        print ("Zero")
    case x if x > 0: # x é um parâmetro, necessário para aplicar a lógica de > 0. Sem ele dá erro de sintaxe
        print ("Positivo")
    case _:
        print ("Negativo")


# def teste1 ():
#     escolha  =  'z'

#     match escolha:
#         case 'z':
#             print('Acertou ')
#         case _:
#             print('errou') 

# # teste1()
# time = timeit.timeit(teste1, number=10)
# print('função1', time)

