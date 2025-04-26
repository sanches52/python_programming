
# EXERCÍCIOS

print('\n <<<< EXERCÍCIOS >>>> \n')

# - CRIE UM MERCADO 

# - UTILIZE LISTAS
# - MOSTRAR O VALOR (módulo separado)**
# - FAZER O PAGAMENTO (módulo separado)
# - FINALIZAR A COMPRA
# - SE DESPEDIR DO USUÁRIO   
# - UTILIZE PARÂMETROS

from mostrar_valor import mostrar_valor
from fazer_pagamento import pagamento

def mercado():
    lista_produtos = ['a','b','c']
    print('Produtos', lista_produtos)

    lista_valores  = [10,20,30]
    print('R$', lista_valores)

    carrinho = []
    valor_pagar = [] 

    pedido = input('Deseja efetuar o pedido s/n')
    while pedido == 's':
          escolha =  int(input('Escolha o produto através do ID'))
          carrinho.append(lista_produtos[escolha])
          valor_pagar.append(lista_valores[escolha])
          print(carrinho)
          print(valor_pagar)
          pedido = input('Deseja efetuar o pedido s/n')
    else: 
         mostrar = mostrar_valor(valor_pagar)
         print('R$',mostrar )  
    print('valor a pagar: R$',mostrar )   
    pagamento()     
         
          

mercado()

# -------------------------------------------

def pagamento():
    print('1  - PIX | 2 -  CC | 3 - CD | 4 -  DINHEIRO')
    formas =  ['pix', 'cc','cd','dinheiro']
    pag = int(input('Digite a opção de pagamento: '))
    if pag == 0:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    elif pag == 1:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    elif pag == 2:     
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])  
       print()  
       print('Obrigada volte sempre')
    elif pag== 3:
       print('FORMA DE PAGAMENTO:')
       print(formas[pag])
       print()
       print('Obrigada volte sempre')
    else:
       print('Essa forma não existe')                

# -------------------------------------------

def mostrar_valor(soma_total):
    soma = sum(soma_total)
    return soma
 
# -------------------------------------------
 
          
      
      
      
      
      
      
      