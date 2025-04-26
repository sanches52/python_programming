
##############################################################
# >>>>>> FUNÇÕES CALCULADORA <<<<<<
##############################################################

from aula10_modulos_divisao import divisao
from aula10_modulos_multiplicacao import multiplicacao
from aula10_modulos_soma import soma
from aula10_modulos_subtracao import subtracao

def calculadora():
    n1 = float(input('Digite o 1º número >> '))
    op = input('Qual operação deseja? (+ - / *) >> ')

    if op == '+': 
       n2 = float(input('Digite o 2º número >> ')) 
       s  = soma(n1,n2)
       print(s)
    elif op == '-': 
       n2 = float(input('Digite o 2º número >> ')) 
       s  = subtracao(n1,n2)
       print(s)
    elif op == '*': 
       n2 = float(input('Digite o 2º número >> ')) 
       s = multiplicao(n1,n2)
       print(s)
    elif op == '/': 
       n2 = float(input('Digite o 2º número >> ')) 
       s = divisao(n1,n2)
       print('=', s)       

calculadora()