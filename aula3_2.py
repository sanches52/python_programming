# Calculadora Simples

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print("SOMA: ", num1 + num2)

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print("SUBTRAÇÃO: ", num1 - num2)

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print("MULTIPLICAÇÃO: ", num1 * num2)

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
print("DIVISÃO: ", num1 / num2)

# Calculadora Simples - Outra maneira

numero_1 = float(input('Digite o 1º número: '))
numero_2 = float(input('Digite o 2º número: '))
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2

print(f'''

<< EXEMPLO: CALCULADORA BÁSICA >>

    SOMA = {soma}
    SUBTRAÇÃO = {subtracao}
    MULTIPLICAÇÃO = {multiplicacao}
    DIVISÃO = {divisao}
''')
