# EXERCÍCIOS

print('\n <<<< ATIVIDADE 2 >>>> \n')

# Crie um sistema de notas alunos, com as seguintes operações:

# ***Utilize While (loop infinito) ou for (loop finito)*** 

# # Sistema de notas de alunos

# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada 
# - Inserir notas 
# - Fazer a média

dic_alunos_notas = {
    'Ana': 0,
    'Paulo': 0,
    'Jessica': 0
}

dic_usuario_senha = {
    'fernando': '123',
    'Cardoso': '456',
    'julia': '789',
    'FELIPE': '6252'
}

print('\n<<<<< BEM-VINDO AO SISTEMA DE NOTAS DOS ALUNOS >>>>>\n')

for i in range(1,4):

    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    # if login == '@julia' and senha == '123456':
    if login in dic_usuario_senha.keys() and senha in dic_usuario_senha.values():

        print('\n>>>>> Cadastre aqui as notas dos alunos: ')

        # nomes = [x for x in notas.keys()]
        # print(nomes)

        notas = []
        nomes = []

        for chave, valores in dic_alunos_notas.items():

            nomes.append(chave)
            notas.append(valores)

            print('\n> Digite as notas do(a) aluno(a): ', chave.upper())  

            nota1 = float(input('\nDigite a 1ª nota: '))
            nota2 = float(input('Digite a 2ª nota: '))
            nota3 = float(input('Digite a 3ª nota: '))

            dic_alunos_notas[chave]= [nota1, nota2, nota3]
            media = sum(dic_alunos_notas[chave]) / len(dic_alunos_notas[chave])

            print('\nA média deste aluno é: ', round(media, 2))

        else:
            break 

    else:
        print('\nAcesso negado!')

else:
    print('\nConta bloqueada!')
         

i = input('\nDigite enter para sair: ')