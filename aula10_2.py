print('\n <<<< AULA 10 >>>> \n')

##############################################################
# >>>>>> ESCOPO DE FUNÇÕES: VARIÁVEIS GLOBAIS <<<<<<
##############################################################

# Variáveis globais:  podem ser utilizadas fora das funções, ou em qualquer lugar do código.

carga = float(input('Digite hora trabalhada/mês: '))
salario =  float(input('Digite o salário: '))
qtd_hora_extra = float(input('\nQuantidade horas extras realizadas: '))
qtd_add_notuno = int(input('Quantidade horas noturnas realizadas: '))
calculo_hora = salario / carga
extra = calculo_hora * 1.5
hex_n = calculo_hora * 1.2


def valorhora():
    print('\nValor da hora: R$', round(calculo_hora,2))
    print('Valor da hora extra (50%): R$', round(extra,2))
    print('Quantidade realizada horas extras: ', round(qtd_hora_extra,2) )
    print('Valor do adicional noturno (20%): R$', round( hex_n,2))
    print('Quantidade realizada adicional noturno: ', round(qtd_add_notuno,2) )

# RETURN (reutilizável em outros ambientes do código) X PRINT (não reutilizável)

def sistema_de_horas():
    print('Seja bem-vindo ao sistema de horas!\n')
    
    # opcoes = ['','Horas'  ]
    escolha = input('Deseja fazer o calculo de horas? (s/n)').lower()
    if escolha == 's':
        valorhora() 
    else:
        print('Saindo do sistema...')    

sistema_de_horas()