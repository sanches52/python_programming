# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. 
# O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento 
# das diárias***.


# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*
# ***O sistema não deve usar loops (for, while) nem funções.**
# O código deve considerar todos os casos possíveis de escolha dos clientes.*

escolha1_reservas = input('Deseja a fazer a reserva? (s/n)')
if escolha1_reservas == 's':

    # - *Cadastro de Cliente:*
    clientes = []
    idades = []

    nome1,idade1 = input('Nome:'),input('Idade:')
    nome2,idade2 = input('Nome:'),input('Idade:')
    nome3,idade3 = input('Nome:'),input('Idade:')

    clientes += (nome1,nome2,nome3)
    idades +=(idade1,idade2, idade3)
    print('Quartos disponiveis:')
    print('0 - Simples | 1 - Duplo | 3 - Luxo')
    lista_quartos = [100.,200.,250.]
    
    # - *Reservas de Quartos:*
    tipo_qua_c1, quant_dias_c1 = int(input('Tipo Quarto 1:')),int(input('Dias c1:'))
    tipo_qua_c2, quant_dias_c2 = int(input('Tipo Quarto 2:')),int(input('Dias c2:'))
    tipo_qua_c3, quant_dias_c3 = int(input('Tipo Quarto 3:')),int(input('Dias c3:'))
        
    # - *Cálculo da Estadia:*
    calculo_c1 = lista_quartos[tipo_qua_c1] * quant_dias_c1
    calculo_c2 = lista_quartos[tipo_qua_c2] * quant_dias_c2
    calculo_c3 = lista_quartos[tipo_qua_c3] * quant_dias_c3
    
    print('R$ cliente 1', calculo_c1)
    print('R$ cliente 2', calculo_c2)
    print('R$ cliente 3', calculo_c3)

    # *Pagamento:*
    lista_pag = ['pix','cc', 'cd']

    forma1 =  input('Digite a forma de pagamento: ')
    forma2 =  input('Digite a forma de pagamento: ')
    forma3 =  input('Digite a forma de pagamento: ')

    if forma1 == lista_pag[0]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma1)
    elif forma1 == lista_pag[1]:
        print('Obrigada volte sempre',clientes[1] )
        print('Sua forma de pagamento é ', forma1)    
    elif forma1 == lista_pag[2]:
        print('Obrigada volte sempre',clientes[2] )
        print('Sua forma de pagamento é ', forma1) 
    else:
        print('Digite algo valido')    


    if forma2 == lista_pag[0]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma2)
    elif forma2 == lista_pag[1]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma2)    
    elif forma2 == lista_pag[2]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma2)         


    if forma3 == lista_pag[0]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma3)
    elif forma3 == lista_pag[1]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma3)    
    elif forma3 == lista_pag[2]:
        print('Obrigada volte sempre',clientes[0] )
        print('Sua forma de pagamento é ', forma3) 

else:
    print('Obrigada volte sempre')




