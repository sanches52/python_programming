
desafio mercado.py

mercado.py

# CRIE UM MERCADO 

# - ESCOLHER UM PRODUTO (módulo separado)

# - UTILIZE LISTAS
# - MOSTRAR O VALOR (módulo separado)**
# - FAZER O PAGAMENTO (módulo separado)
# - FINALIZAR A COMPRA
# - SE DESPEDIR DO USUÁRIO   
# - UTILIZE PARÂMETROS

from fazer_pedido import fazer_pedido
from pagamento import pagamento


def mercado():
    fazer_pedido()
    pagamento()




mercado()    


fazer_pedido.py
def fazer_pedido():
    meu_carrinho = []
    meus_valores  = []
    lista = ['a','b','c']
    valores = [150,50,20]
    inicio =  input('deseja fazer o  pedido: ')
    while inicio == 's':
          print(1 - 'a', 2 - 'b', 3 -'c')
          meus_pedidos = int(input('Faça seu pedido'))
          meu_carrinho.append(lista[meus_pedidos])
          meus_valores.append(valores[meus_pedidos])
          inicio =  input('deseja fazer o  pedido: ')
          
    print(meu_carrinho)
    soma = sum(meus_valores)
    print('R$',soma)


pagamento.py
def pagamento():
    
    forma_pagamento =  input('Deseja realizar outro pagamento? S/N')            
    while forma_pagamento == 's':
            print(f'''1 -  PIX
            2 -  cc
            3 -   cd
            4 - DINHEIRO''')
            escolha = input('>>')
            if escolha == '1':
                print('Pagamento realizado com pix')
            elif escolha == '2':
                print('Pagamento realizado com CC')
            elif escolha == '3':
                print('Pagamento realizado com CD')
            elif escolha =='4':
                print('pagamento relizado com dinheiro') 
            else: 
                print('Essa opção não existe')
            forma_pagamento =  input('Deseja realizar outro pagamento? S/N')
            if forma_pagamento == 'n': print('Até logo')          
         


    

from media import media 
from mediana import mediana
from  statistics import *
 
 





# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA 
#PARA UMA ESCOLA. 
# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE 
# COM ESTATISTICA A MODA E A MEDIA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES 
# 1 -  ***VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***
# 2 - ***OU USAR STATISTICS *****

def system():
    alunos = []
    notas  = []

    insert = input('deseja inserir as notas')
    while insert ==  's':
          nome = input('Digite o nome do aluno')
          nota = int(input('nota: '))   
          notas.append(nota)
          alunos.append(nome) 
          insert = input('deseja inserir as notas')

          print(f'''Alunos: {alunos}  - Notas  {notas}''')
          m1 = media(notas)
          m2 = mediana(notas)
          print('Media', m1,'mediana',  m2)
          moda  =  mode(notas )
          print(moda)


        #   d1 = desvio(notas)
        #   m3 = mod(notas)
        #   print(d1, m3)
          



    else: 
       pass
        #  m1 = media(notas)
        #  m2 = mediana(notas)
        #  m3 = moda(nota)
        #  d1 = desvio(notas)
        #  print(m1, m2, m3,d1)
         
          

            # print(f'MEDIA -  {media1}MODA - {moda1}MEDIANA- {mediana1}DESVIO - {desvio1}')                  


system()    
    


     




from statistics import mean


def media(lista):
    media  =  mean(lista)
    return media
























main.py


# ## Desafio 2
# Você é um analista de dados, e decidiu trocar de emprego.
# Utilize a media, moda, mediana e o desvio padrão 
para decidir qual empresa faz sentido para você:
# Justificar por que decidiu por essa empresa.
# ***Verifique isso através dos salários:***

from  media import media1
from mediana import mediana1
from varianca import varianca1
from desvio import desvio1
from moda import moda1


empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900,7000]

def hadle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)


hadle(empresa1, empresa1)  
hadle(empresa2, empresa2)   
hadle(empresa3, empresa3) 
hadle(empresa4, empresa4) 
 
 
 
 
 moda.py
 
 import statistics

def moda1(lista):
    moda = statistics.mode(lista)
    print('Moda: ', moda)
    
    
 mediana.py
 import statistics

def mediana1(lista):
    mediana = statistics.median(lista)
    print('Mediana: ', mediana)
 
 
 
 varianca.py
 
 import statistics

def varianca1(lista):
    varianca = statistics.variance(lista)
    print('Variança: ', varianca)
 
 
 
desvio.py
import statistics

def desvio1(lista):
    desvio = statistics.stdev(lista)
    print(f'Desvio padrão:  {desvio:.2f}')
 
 
 
 
 media.py
 
 import statistics

def media1(lista):
    media = statistics.mean(lista)
    print('Media: ', media)
 
 
 
 
 
 
 
 ----------------------
 
 import statistics


def moda(lista):
    moda = statistics.mode(lista)
    print('moda', moda)

def media(lista):
    media = statistics.mean(lista)
    print('media', media)

def mediana(lista):
    mediana = statistics.median(lista)
    print('mediana',mediana)

def desvio(lista):
    desvio = statistics.stdev(lista)
    print("Desvio:", desvio) 


def display():
    print('Empresa 1')
    empresa1 = [1000,6000,1200,8000,1400]
    desvio(empresa1)
    moda(empresa1)
    mediana(empresa1)
    media(empresa1) 

    print('--------------------------')  

    print('Empresa 2')
    empresa2 = [5000,4000,3000,2000,7000]
    desvio(empresa2)
    moda(empresa2)
    mediana(empresa2)
    media(empresa2) 

    print('--------------------------') 

    print('Empresa 3')
    empresa3 = [1200,1300,8000,3000,15000]
    desvio(empresa3)
    moda(empresa3)
    mediana(empresa3)
    media(empresa3) 

    print('--------------------------')

    print('Empresa 4')
    empresa4 = [1400,1750,2000,4500,5900]
    desvio(empresa4)
    moda(empresa4)
    mediana(empresa4)
    media(empresa4) 
    
    print('--------------------------')        
            
    
display()






 
 
 
 
 
 
 --------------------------------------------------------------
 
 
 
 
 
 
 
 
 
from desvio_py import *  
from moda import moda
from media import media
from mediana import mediana
from statistics import stdev, StatisticsError

def desvio(lista):

    try:
        return float(stdev(lista))
        
    except StatisticsError as erro:
        return erro  

def system():
    alunos = []
    notas  = []

    while True:
        insert = input('Deseja inserir as notas? (s/n): ').strip().lower()
        if insert == 's':
            nome = input('Digite o nome do aluno: ').strip()
            try:
                nota = float(input('Nota: '))
                notas.append(nota)
                alunos.append(nome)
            except ValueError:
                print('Por favor, insira um número válido para a nota.')
                
            
         
            m1 = media(notas)
            m2 = mediana(notas)
            moda1 = moda(notas)
            d1 = desvio(notas)
           
          
            print(f'Alunos: {alunos}')
            print(f'Notas: {notas}')
            print(f'Média: {m1}')
            print(f'Mediana: {m2}')
            print(f'Moda: {moda1}')
            print(f'Desvio padrão: {d1}')
        elif insert == 'n':
            return notas
            
        else:
            print('Opção inválida. Por favor, digite "s" para sim ou "n" para não.')
            
system()


-----------------------

from statistics import stdev
from main import *


def desvio(lista):
    d = stdev(lista)
    return d

l = [1.0,5.0]
d = desvio(l)

print(d)
