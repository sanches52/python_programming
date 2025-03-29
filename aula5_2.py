print('\nEx.1\n')
print('Bem-vindo!')


print('\nEx.2\n')
x = True
print(type(x))


print('\nEx.3\n')
x = float(input('Digite o primeiro número decimal: '))
y = float(input('Digite o segundo número decimal: '))
print('A multiplicação dos números é: ', x * y)

print('\nEx.4\n')
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
print('A divisão dos números é: ', x / y)


print('\nEx.5\n')
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
print('A subtração dos números é: ', x - y)


print('\nEx.6\n')
x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
print('A divisão inteira dos números é: ', x // y)


print('\nEx.7\n')
x = int(input('Digite o primeiro número decimal: '))
y = int(input('Digite o segundo número decimal: '))
z = int(input('Digite o terceiro número decimal: '))
a = int(input('Digite o quarto número decimal: '))
print('A multiplicação dos números é: ', x * y * z * a)


print('\nEx.8\n')
num = int(input('Digite o número inteiro: '))
print('O dobro do número é: ', num * 2)


print('\nEx.9\n')
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
data_nascimento = input('Digite sua data de nascimeto (dd/mm/aaaa): ')
endereco = input('Digite seu endereco completo: ')
estado = input('Digite seu estado: ')
uf = input('Digite sua UF: ')
telefone_celular = int(input('Digite seu telefone celular (somente números): '))
cpf = int(input('Digite seu CPF (somente números): '))

print(f'''

    Aqui está seu cadastro {nome.upper()} {sobrenome.upper()}:

    DATA NASCIMENTO:  {data_nascimento}
    ENDEREÇO:  {endereco}
    ESTADO:  {estado}
    UF:  {uf}
    CELULAR:  {telefone_celular}
    CPF:  {cpf}

''')

