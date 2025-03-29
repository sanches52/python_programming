# <<<< EXERCÍCIOS >>>>

#1 - Crie um programa para efetuar a leitura de um número inteiro e
#apresentar o resultado do quadrado deste número.

print('\nEx1)\n')

num = int(input('Digite um número inteiro: '))

squared_num = num ** 2 

print('O quadrado deste número é: ', squared_num)


#2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome.
#Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

print('\nEx2)\n')

nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu último nome: ')

print('Seu nome completo é: ', nome, sobrenome)

#3 - Peça ao usuário para digitar dois números inteiros e armazene-os
#em variáveis. Realize a concatenação desses números como strings e
#exiba o resultado.

print('\nEx3)\n')

num1 = input('Digite o 1º numero inteiro: ')
num2 = input('Digite o 2º numero inteiro: ')

print('Os números concatenados são: ', str(num1), str(num2))

#4 - Crie uma variável para armazenar a palavra "Python".
#Em seguida, adicione um número inteiro ao final da palavra usando a
#concatenação e exiba o resultado.

print('\nEx4)\n')

python = "Python"

print(python, 3879)

#5 - Declare uma variável contendo uma frase.
#Em seguida, peça ao usuário para digitar uma palavra e
#concatene essa palavra no final da frase. Exiba o resultado. 

print('\nEx5)\n')

frase = 'O mar é azul! '

palavra = input('Digite uma palavra: ')

print(frase, palavra)
