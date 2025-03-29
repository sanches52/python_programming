# Funções básicas incorporadas no Python

# print(), len(), type(), int(), float(), str(), list(), tuple()
# Olhar todas as variáveis incorporadas no site oficial do Python: https://docs.python.org/3/library/functions.html

print('\n <<<< AULA 6 >>>> \n')
name = 'Python'
name_list = list(name)
print(name_list)

name = 'Python'
name_tuple = tuple(name)
print(name_tuple)


lista = list(range(1,11,5))


tamanho = len(lista)
soma = sum(lista)
menor = min(lista)
maior = max(lista)

print('O tamanho da lista é: ', tamanho)
print('A soma da lista é: ', soma)
print('O máximo da lista é: ', maior)
print('O mínimo da lista é: ', menor)

lista2 = [10,4,76,82,23,93,14,55,43]
print('Esta é a lista original: ', lista2)
print('Esta é a lista ordenada: ',sorted(lista2))

print('\n <<<< EXERCÍCIOS >>>> \n')

# EXERCÍCIOS

num1 = 4
num2 = 6
num3 = 2
calc = (num1 * num2 ) // num3
print('1) Multiplique 4 por 6 e divida o resultado por 2:', calc)

num1 = 5
num2 = 7
calc = num1+num2
print('2) Calcule a soma de 5 e 7:', calc)

num1 = 3
num2 = 4
calc = num1**num2
print('3) Eleve 3 à potência de 4:', calc)

num1 = 8
num2 = 12
num3 = 15
calc = round((num1 + num2 + num3) / 3, 2)
print('4) Calcule a média de 8, 12 e 15:', calc)

num1 = 10
num2 = 2
num3 = 5
calc = (num1 - num2) * num3
print('5) Subtraia 10 de 2 e multiplique o resultado por 5:', calc)

num1 = 27
num2 = 3
num3 = 5
calc = (num1 // num2) + num3
print('6) Divida 27 por 3 e some 5:', calc)

num1 = 17
num2 = 4
calc = (num1 % num2)
print('7) Calcule o módulo de 17 por 4:', calc)

num1 = 9
num2 = 3
calc = (num1 * num2) ** 2
print('8) Multiplique 9 por 3 e, em seguida, eleve o resultado ao quadrado:', calc)

num1 = 81
num2 = (1/2)
calc = int((num1) ** num2)
print('9) Calcule a raiz quadrada de 81:', calc)

num1 = 3
num2 = 4
num3 = 20
calc = (num1 * num2) + num3
print('10) Adicione 20 a 3 vezes 4:', calc)

num1 = 15
num2 = 2
num3 = 7
calc = (num1 * num2) - num3
print('11) Multiplique 15 por 2 e, em seguida, subtraia 7:', calc)

num1 = 5
num2 = 3
calc = (num1) ** num2
print('12) Eleve 5 ao cubo:', calc)

num1 = 17
num2 = 21
num3 = 25
calc = round((num1 + num2 + num3) / 3, 2)
print('13) Calcule a média de 17, 21 e 25:', calc)

num1 = 11
num2 = 2
num3 = 7
calc = (num1 * num2 ) + num3
print('14) Multiplique 11 por 2 e adicione 7:', calc)

num1 = 3
num2 = 8
num3 = 15
num4 = 2
calc = ((num1 * num2 ) - num3) / num4
print('15) Subtraia 15 de 3 vezes 8 e divida o resultado por 2:', calc)

num1 = 2
num2 = 10
calc = num1 ** num2
print('16) Eleve 2 à potência de 10:', calc)