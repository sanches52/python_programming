print('\n <<<< AULA 8 >>>> \n')

##############################################################
# >>>>>> CONDICIONAIS <<<<<<
##############################################################

print('Sintaxe padrão: CONDICIONAL\n')
if 10 == 2: # True
    print('10 é igual a 2\n')
elif 10 < 2:
    print('10 é menor que 2\n')    
else:
    print('10 é maior que 2\n')   

# >>>> Exemplo1: Acertar um número randômico

# import random

# numero = random.randint(1,10)
# chute = int(input('Ex1) Faça sua aposta de um número de 1 a 10: '))

# if numero == chute:
#     print('Acertou em cheio! O número certo é: ', numero)
# else:
#     print('Errou feio! O número certo é: ', numero)

# >>>> Exemplo2: Mapear ingredientes para fazer bolo

# carteira_motorista = input('\nEx2) Possui CNH? (s/n) ')
# idade = int(input('Digite sua idade: '))


# if carteira_motorista == 's' or idade >= 18:
#     print('Habilitado, pode dirigir!')
# else:
#     print('Não pode dirigir!')   

# >>>> Exemplo3: Mapear ingredientes para fazer bolo

# condimentos = input('\nEx3) Possui farinha, açucar, ovos e leite? (s/n) ')
# microondas = input('Microondas? (s/n) ')
# airfrayer = input('Ayrfryer? (s/n) ')
# forno = input('Forno? (s/n) ')


# if condimentos == 's' and microondas == 's' or airfrayer == 's' or forno == 's':
#     print('Tudo OK! Comece a fazer o bolo.')
# else:
#     print('Sem chances de fazer o bolo!')   

# >>>> Exemplo4: Sistema Escolar

alunos = {
        'Ana':[10,9,8,5.5,3,7,10],
        'Fernanda':[1,2,3,6,5,2,7],
        'Leonardo':[10,10,10,10,10,10,10]
     }

# Extraindo notas para variável
notas_ana = alunos['Ana']
notas_fernanda = alunos['Fernanda']
notas_leonardo =alunos['Leonardo']

# Maior nota por aluno
maior_nota_ana = max(notas_ana)
maior_nota_fernanda = max(notas_fernanda)
maior_nota_leonardo = max(notas_leonardo)

# Média por aluno
media_ana = sum(alunos['Ana']) / len(alunos['Ana'])
media_fernanda = sum(alunos['Fernanda'])/len(alunos['Fernanda'])
media_leonardo = sum(alunos['Leonardo'])/len(alunos['Leonardo'])

# Média total
medias = [media_ana, media_fernanda, media_leonardo]
media_total = sum(medias) / len(medias)

# Maior média (aluno)
lista_nomes = ['Ana','Fernanda','Leonardo']
maior_media = max(medias)
indice_maior_media = medias.index(maior_media)

# Mediana
mediana_ana = notas_ana[3:4]
mediana_fernanda = notas_fernanda[3:4]
mediana_leonardo = notas_leonardo[3:4]

# Amplitude
amplitude_ana = maior_nota_ana - min(notas_ana)
amplitude_fernanda = maior_nota_fernanda - min(notas_fernanda)
amplitude_leonardo = maior_nota_leonardo - min(notas_leonardo)

# Moda
notas_ana.sort()
notas_fernanda.sort()
notas_leonardo.sort()

moda_ana = max(set(notas_ana), key=notas_ana.count)
moda_fernanda = max(set(notas_fernanda), key=notas_fernanda.count)
moda_leonardo = max(set(notas_leonardo), key=notas_leonardo.count)


print('\n<<<< BEM-VINDO AO SISTEMA ESCOLAR! >>>>\n')

# 1) Média Total de notas: soma() / len()
# 2) Média de cada aluno: soma() / len()
# 3) Moda (ordenar a lista e encontrar valor do meio) / Mediana / Amplitude (valor máx - mín)
# 4) Maior nota de cada aluno: max()
# 5) Maior média: max()

print('Escolha a opção desejada: ')
print ('\n1) Média Total \n2) Média por aluno \n3) Moda / Mediana / Amplitude \n4) Maior nota por aluno \n5) Maior média (aluno)')
escolha = input('\nDigite o que deseja visualizar: ')

if escolha == '1':
    print('Média Total: ', round((media_total),2))

elif escolha == '2':
    print('Média por aluno\n')
    print('Ana: ', round((media_ana),2))
    print('Fernanda: ', round((media_fernanda),2))
    print('Leonardo: ', round((media_leonardo),2))

elif escolha == '3':
    print('Moda | Mediana | Amplitude\n')
    print('Moda (Ana): ', moda_ana)
    print('Mediana (Ana): ', mediana_ana)
    print('Amplitude (Ana): ', amplitude_ana)
    print('----------------------'*2)
    print('Moda (Fernanda): ', moda_fernanda)
    print('Mediana (Fernanda): ', mediana_fernanda)
    print('Amplitude (Fernanda): ', amplitude_fernanda)
    print('----------------------'*2)
    print('Moda (Leonardo): ', moda_leonardo)
    print('Mediana (Leonardo): ', mediana_leonardo)
    print('Amplitude (Leonardo): ', amplitude_leonardo)

elif escolha == '4':
    print('Maior nota por aluno\n')
    print(f'Maior nota (Ana) - {maior_nota_ana}\nMaior nota (Fernanda) - {maior_nota_fernanda}\nMaior nota (Leonardo) - {maior_nota_leonardo} ')

elif escolha == '5':
    print('\nMaior Media é de:', lista_nomes[indice_maior_media],'(',maior_media,')')

else:
    print('Opção inválida. Digite um número do menu.')   


   