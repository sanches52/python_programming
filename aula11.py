print('\n <<<< AULA 11 >>>> \n')

##############################################################
# >>>>>> TRY / EXCEPT <<<<<<
############################################################## 

# Fundamental para lidar com exceções, ou seja, situações inesperadas ou erros que podem ocorrer durante a execução de um programa.

    # try:
    #     Protected code that might trigger an exception

    # except:
    #     Handle exception properly

    # else: 
    #     Only when no exceptions

    # finally:
    #     Always run this code

# Doc c/ tipos de erros:
# https://docs.python.org/pt-br/3/tutorial/errors.html

##############################################################
# >>>>>> ERROS FAMOSOS <<<<<<
############################################################## 

    # TypeError
    # Surge quando uma função ou operação é aplicada a um objeto de tipo incorreto

    # UnboundLocalError
    # Surge quando uma referência é feita para uma variável local em uma função ou método, porém nenhum valor está preso à variável

    # UnicodeError
    # Surge quando existe um erro relacionado a Unicode codificação ou decodificação

    # UnicodeEncodeError
    # Surge quando um erro de codificação de Unicode ocorre

    # UnicodeDecodeError
    # Surge quando um erro de decodificação de Unicode ocorre

    # UnicodeTranslateError
    # Surge quando um erro de tradução de Unicode ocorre

    # ValueError
    # Surge quando uma função pega um argumento de tipo correto, porém de valor impróprio

    # ZeroDivisionError
    # Surge quando a segunda divisão ou módulo é zero

a = int(input())
b = int(input())

try:
      print(a/b)

except ZeroDivisionError as error:
      print(error)

else:
      print('Sem erros')

finally:
      print('Aqui sempre vai printar')

# ----------------------------------------------------

def trantando_erros():
    try: 
        numero = int(input('>>'))
    except ZeroDivisionError as erro:
        print(erro)
    except ValueError as erro2:
        print('Erro no valor da variável')  
    except NameError as erro:
        print(erro)      
    finally:
        print('O sistema foi carregado')

trantando_erros()

# ----------------------------------------------------

def divisao():

    try:
      n1 = float(input('>>'))
      n2 = float(input('>>'))
      div = n1/n2
      print(div)  
    except ZeroDivisionError:
        print("A divisão não ser por zero")
    except ValueError:
        print('Um texo foi digitado')
    except TypeError as erro:
        print(erro)

    else:
        print('Algo deu errado ')    

divisao() 

import statistics 

def divisao():
    try:
     lista=[0,2,1 , 5]
     moda  =  statistics.mode(lista)
     print(moda)
    except ZeroDivisionError as erro:
        print(erro)
    except TypeError:
        print('Provavelmente digitaram letras')
    except ValueError as erro :
        print(erro)
    except NameError as erro:
        print(erro)    
    except SyntaxError as erro:
        print(erro)     
    finally:
        print('Carregamento finalizado')


divisao()        


  