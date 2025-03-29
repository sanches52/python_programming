# input() print() variáveis  + - * / | > < >= <= !=

# sistema de notas de escola / média 

print('Sistema de Notas de Escola\n')

nome = input('Digite o nome do Aluno: ')

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))
nota5 = float(input('Digite a 5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

#print('Aluno: ')
#print(nome)
#print(media)

aprovado = media >= 7
reprovado = media < 5
recuperacao = media >= 5 and media < 7

# concatenar - juntar
print('\nNome do Aluno: ', nome)
print('Média: ', media)
print(f'''
      Notas:
      1ª nota: {nota1}
      2ª nota: {nota2}
      3ª nota: {nota3}
      4ª nota: {nota4}
      5ª nota: {nota5}
''')

print('Aprovado - ', aprovado)
print('Em Recuperação - ', recuperacao)
print('Reprovado - ', reprovado)
