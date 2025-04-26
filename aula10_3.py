print('\n <<<< AULA 10 >>>> \n')

##############################################################
# >>>>>> FUNÇÕES: PARÂMETROS E RETURN <<<<<<
##############################################################

def calculo_hora(carga, salario):
    return carga / salario

def calculo_extra_50(hora):
    return hora * 1.5

def calculo_hora_noturna(hora):
    return hora * 1.2

def cumprimentar(nome):
    print('Olá', nome, ', seja bem-vindo ao Sistema de Horas!\n')

def sistema_de_horas():
    nome = input('Qual seu nome? ')
    cumprimentar(nome)

    escolha = int(input('1) Valor/hora', '2) Extra (50%)','3) Adicional Noturno (20%)'))

    if escolha == 1:
        carga = float(input('Carga de trabalho mês: '))
        salario =  float(input('Digite o salario: ')) 
        print('R$', round(calculo_hora(carga,salario),2))

    elif escolha == 2:
        carga = float(input('Carga de trabalho mês: '))
        salario =  float(input('Digite o salario: ')) 
        valor_hora  =  calculo_hora(carga,salario)
        print('Hora Extra (50%):',round(calculo_extra_50(valor_hora),2))  
        
    elif escolha == 3:
        carga = float(input('Carga de trabalho mês: '))
        salario =  float(input('Digite o salario: ')) 
        valor_hora  =  calculo_hora(carga,salario)
        print('Adicional Noturno Extra (20%):',round(calculo_hora_noturna(valor_hora),2))   

    else:
        print('Opção inválida! Digite algo válido')   


sistema_de_horas()