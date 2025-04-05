# DESAFIO CONDICIONAIS

print('\n <<<< SISTEMA RESERVA DE HOTÉIS >>>> \n')

# >>> CADASTRO DE CLIENTES
# opcao1 = input('Deseja cadastrar o 1º cliente? (s/n) ')
# opcao2 = input('Deseja cadastrar o 2º cliente? (s/n) ')
# opcao3 = input('Deseja cadastrar o 3º cliente? (s/n) ')

# if opcao1 == 's':
#     cliente1 = input('Nome do 1º cliente: ')
#     idade1 = int(input('Idade do 1º cliente: '))
# else:
#     cliente1 = []
#     idade1 = []

# if opcao2 == 's':
#     cliente2 = input('Nome do 2º cliente: ')
#     idade2 = int(input('Idade do 2º cliente: '))
# else:
#     cliente2 = []
#     idade2 = []

# if opcao3 == 's':
#     cliente3 = input('Nome do 3º cliente: ')
#     idade3 = int(input('Idade do 3º cliente: '))
# else:
#     cliente3 = []
#     idade3 = []

escolha_reserva = input('Deseja fazer uma reserva? (s/n)')

if escolha_reserva == 's':

    cliente_1 = input('Nome do 1º cliente: ')
    idade_1 = int(input('Idade do 1º cliente: '))

    cliente_2 = input('\nNome do 2º cliente: ')
    idade_2 = int(input('Idade do 2º cliente: '))

    cliente_3 = input('\nNome do 3º cliente: ')
    idade_3 = int(input('Idade do 3º cliente: '))

    cliente = []
    idade = []
    cliente += (cliente_1, cliente_2, cliente_3)
    idade += (idade_1, idade_2, idade_3)

    # RESERVA DE QUARTOS

    print('\nTipos de quartos e preços para reserva: ')
    print('''
            1) Simples - R$ 100/dia
            2) Duplo - R$ 150/dia
            3) Luxo - 250/dia
    ''')

    preco_quartos = [100., 150., 250.]

    escolha_1 = int(input(f'{cliente[0]}, qual quarto deseja? (1/2/3) '))
    dias_1 = int(input(f'E {cliente[0]}, quantos dias pretende reservar? '))

    escolha_2 = int(input(f'\n{cliente[1]}, qual quarto deseja? (1/2/3) '))
    dias_2 = int(input(f'E {cliente[1]}, quantos dias pretende reservar? '))

    escolha_3 = int(input(f'\n{cliente[2]}, qual quarto deseja? (1/2/3) '))
    dias_3 = int(input(f'E {cliente[2]}, quantos dias pretende reservar? '))

    escolha_quarto = []
    qtd_dias = []
    escolha_quarto += (escolha_1, escolha_2, escolha_3)
    qtd_dias += (dias_1, dias_2, dias_3)

    # PAGAMENTO DAS DIÁRIAS

    # CLIENTE 1

    ##############################################################
    # >>>>>> TERMINAR!!!
    if cliente.index() is not null and escolha_quarto[0] == 1:

        total_cliente1 = preco_quartos[0] * qtd_dias[0]
        print(f'\n> {cliente[0]}, você vai pagar: R$ ', total_cliente1)

    elif index(cliente) == 0 and escolha_quarto[0] == 2:

        total_cliente1 = preco_quartos[1] * qtd_dias[0]
        print(f'\n> {cliente[0]}, você vai pagar: R$ ', total_cliente1)

    elif index(cliente) == 0 and escolha_quarto[0] == 3:

        total_cliente1 = preco_quartos[2] * qtd_dias[0]
        print(f'\n> {cliente[0]}, você vai pagar: R$ ', total_cliente1)

    else:
        print('Opção inválida. Digite um número válido (1/2/3).')

    # CLIENTE 2
    if index(cliente) == 1 and escolha_quarto[0] == 1:

        total_cliente2 = preco_quartos[0] * qtd_dias[1]
        print(f'\n> {cliente[1]}, você vai pagar: R$ ', total_cliente2)

    elif index(cliente) == 1 and escolha_quarto[0] == 2:

        total_cliente2 = preco_quartos[1] * qtd_dias[1]
        print(f'\n> {cliente[1]}, você vai pagar: R$ ', total_cliente2)

    elif index(cliente) == 1 and escolha_quarto[0] == 3:

        total_cliente2 = preco_quartos[2] * qtd_dias[1]
        print(f'\n> {cliente[1]}, você vai pagar: R$ ', total_cliente2)

    else:
        print('Opção inválida. Digite um número válido (1/2/3).')

    # CLIENTE 3
    if index(cliente) == 2 and escolha_quarto[0] == 1:

        total_cliente3 = preco_quartos[0] * qtd_dias[2]
        print(f'\n> {cliente[2]}, você vai pagar: R$ ', total_cliente3)

    elif index(cliente) == 2 and escolha_quarto[0] == 2:

        total_cliente3 = preco_quartos[1] * qtd_dias[2]
        print(f'\n> {cliente[2]}, você vai pagar: R$ ', total_cliente3)

    elif index(cliente) == 2 and escolha_quarto[0] == 3:

        total_cliente3 = preco_quartos[2] * qtd_dias[2]
        print(f'\n> {cliente[2]}, você vai pagar: R$ ', total_cliente3)

    else:
        print('Opção inválida. Digite um número válido (1/2/3).')

else:
    print('Obrigado, volte sempre!')



