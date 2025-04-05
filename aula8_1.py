# EXERCÍCIOS

print('\n <<<< EXERCÍCIOS >>>> \n')

# **Ex. 1:** Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
numero = float(input('\nEx1) (Verifica se é postivo/negativo/nulo) Digite um número: '))

if numero == 0:
    print('É zero.')
elif numero >= 0:
    print('É positivo.')
else:
    print('É negativo.')

# **Ex. 2:** Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.

idade = int(input('\nEx2) (Verifica se pode votar) Digite sua idade: '))

if idade >= 18:
    print('Já pode votar!')
else:
    print('Ainda não pode votar.')

# **Ex. 3:** Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

number = float(input('\nEx3) (Verifica se é par/ímpar) Digite um número qualquer: '))

if number % 2 == 0:
    print('É par!')
else:
    print('É impar!')

# **Ex. 4:** Usuário vai digitar 3 números, para criar um triângulo. Verifique se um triângulo é equilátero, isósceles ou escaleno
# Um triângulo é equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é isósceles se dois lados possuem a mesma medida. 
# Um triângulo é escaleno se todos os lados possuem medidas diferentes.

var1 = float(input('\nEx3) (Verifica tipo de triângulo) Digite o 1º numero: '))
var2 = float(input('\nEx3) (Verifica tipo de triângulo) Digite o 2º numero: '))
var3 = float(input('\nEx3) (Verifica tipo de triângulo) Digite o 3º numero: '))

if var1 == var2 and var1 == var3 and var2 == var3:
    print('É equilátero!')

elif var1 != var2 and var1 != var3 and var2 != var3:
    print('É escaleno!')

else:
    print('É isósceles!')

# **Ex. 5:** # Determine se um número é múltiplo de 5 e 7.

numero = float(input('\nEx5) (Verifica múltiplo de 5 e 7) Digite um numero: '))

if numero % 5 == 0 and numero % 7 == 0:
    print('É múltiplo!')
else:
    print('Não é múltiplo!')

# **Ex. 6:** # Verifique se um número é positivo e maior que 10.

numero = float(input('\nEx6) (Verifica se é + e >10) Digite um numero: '))

if numero >= 0 and numero == 10:
    print('É positivo e maior que 10!')
else:
    print('Não é positivo e maior que 10!')

# **Ex. 7:** # Verifique se um número é divisível por 3 ou 5.

numero = float(input('\nEx) (Verifica se é divisível por 3 ou 5) Digite um numero: '))

if numero % 3 == 0 or numero % 5 == 0:
    print('É divisível!')
else:
    print('Não é divisível!')

