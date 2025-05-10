print('\n <<<< EXERCÍCIOS >>>> \n')

# ***1: Verificando se o número é par ou ímpar***

num = int(input('Insira aqui um número: '))

match num:
    case num if num % 2 == 0:
        print('Par')
    case _:
        print('Ímpar')

# ***2: Verificando se um número é positivo, negativo ou zero***

num2 = int(input('\nInsira aqui um número: '))

match num2:
    case 0:
        print('Zero')
    case num2 if num2 > 0:
        print('Positivo')
    case _:
        print('Negativo')

# ***3: Verificando se uma string é vazia ou não***

string = input('\nInsira aqui um texto: ')

match string:
    case '':
        print('Texto vazio')
    case _:
        print('Texto não vazio')

# ***4: Verificando se um número é maior, menor ou igual a 10***

num3 = int(input('\nInsira aqui um número: '))

match num3:
    case 10:
        print('Igual a 10')
    case num3 if num3 > 10:
        print('Maior que 10')
    case _:
        print('Menor que 10')

# ***5: Classificando uma idade em faixas etárias -  criança, jovem, adulto, idoso***

idade = int(input('\nInsira aqui sua idade: '))

match idade:
    case idade if idade <= 12:
        print('Criança')
    case idade if idade <= 17:
        print('Adolescente')
    case idade if idade <= 35:
        print('Jovem')
    case idade if idade <= 64:
        print('Adulto')
    case _:
        print('Idoso')