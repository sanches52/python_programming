print('\n <<<< AULA 7 >>>> \n')

##############################################################
# >>>>>> LIST(), TUPLE(), SET(), DICT() <<<<<<
##############################################################

#Listas são mutáveis, ou seja, é permitido alterar os valores dentro dela

print('Esta lista tem uma dimensão (Vetor)')
n = [1,2,3,4,5,6,7,8,9,'10','11','12']
print(n)

print('\nEsta lista tem duas dimensões (Matriz)')
n = [[1,2,3],[4,5,6],[7,8,9], ['10','11','12']]
print(n)

# Exemplo Estrutura de Dados Composta - Tipo Texto

# nome1 = input('\nDigite o 1º nome aqui: ')
# nome2 = input('Digite o 2º nome aqui: ')
# nome3 = input('Digite o 3º nome aqui: ')

# nomes = []

# nomes = [nome1, nome2, nome3]

# print('\nO 3º nome é: ', nomes[2])
# print('O 2º nome é: ', nomes[1])
# print('O 1º nome é: ', nomes[0])

# Exemplo Estrutura de Dados Composta - Tipo Número

print('\n<<< VAMOS BRINCAR DE ALTERAR LISTAS! >>>')

lista_numeros = [2,7,7.8,33.2,92.0,13,[575,743,23,11,84,24,0.5],6592,3956]

print('\nLista ANTES da alteração :', lista_numeros)
print('O tamanho da lista é de', len(lista_numeros), 'índices.')

print('''\n
   > As alterações serão:
        Índice [6][1] recebe valor de 0.5.
        Índice [5] é elevado ao quadrado.
        Índice [8] é dividido por 3.
        Índice [0] é multiplicado por 3296.
        Índice [1] é somado com 1311.
        Índice [6][0] é elevado ao Índice [6][1].
   
''')

lista_numeros[6][1] = 0.5
lista_numeros[5] = lista_numeros[5] ** 2
lista_numeros[8] = lista_numeros[8] // 3
lista_numeros[0] = lista_numeros[0] * 3296
lista_numeros[1] = lista_numeros[1] + 1311
lista_numeros[6][0] = int(lista_numeros[6][0] ** lista_numeros[6][1])

print('Lista DEPOIS da alteração :', lista_numeros)

print('\n> Pergunta 1: os índices [0:2] são iguais a [7:]? ', lista_numeros[7:] == lista_numeros[0:2]) 
print('> Pergunta 2: o índice [6][0:2] é igual [6][5:]? ', lista_numeros[6][0:2] == (lista_numeros[6][5:]))

novo_6_0 = int(input('\nSubstitua o valor de [6][0] para que a Pergunta 2 seja "True": '))

lista_numeros[6][0] = novo_6_0
lista_numeros[6][0] = int(lista_numeros[6][0] ** lista_numeros[6][1])

print('\nLista DEPOIS da alteração :', lista_numeros)
print('\n> Pergunta 2: o índice [6][0:2] é igual [6][5:]? ', lista_numeros[6][0:2] == (lista_numeros[6][5:]))

# <<<<< EXEMPLO MERCADO >>>>>

# produtos = ['arroz', 'feijão','ervilha', 'ração']
# valores = [10.0,5.0,2.0,50.0]

# print('produtos', produtos)

# carrinho = []
# meu_total = []

# escolha1 = int(input('Id do produto'))
# escolha2 = int(input('Id do produto'))
# escolha3 = int(input('Id do produto'))

# carrinho = [produtos[escolha1], produtos[escolha2],produtos[ escolha3]]
# meu_total = [valores[escolha1], valores[escolha2],valores[ escolha3]]

# total = meu_total[0] + meu_total[1]+meu_total[2]

# print('Seus produtos: ', carrinho)
# print('Valores dos seus produtos: ', meu_total)
# print('*******************************************')
# print('R$', total)

# print('Obrigado! Volte sempre!')

# <<<<< EXEMPLO MERCADO COM APPEND >>>>>

# produtos = ['arroz', 'feijão','ervilha', 'ração']
# valores = [10.0,5.0,2.0,50.0]

# print('produtos', produtos)

# carrinho = []
# meu_total = []

# escolha1 = int(input('Id do produto'))
# escolha2 = int(input('Id do produto'))
# escolha3 = int(input('Id do produto'))

# carrinho.append(produtos[escolha1])
# carrinho.append(produtos[escolha2])
# carrinho.append(produtos[escolha3])

# meu_total.append(valores[escolha1])
# meu_total.append(valores[escolha2])
# meu_total.append(valores[escolha3])

# total = meu_total[0] + meu_total[1]+meu_total[2]

# print('Seus produtos', carrinho)
# print('Valores dos seus produtos', meu_total)
# print('*******************************************')
# print('R$', total)

# print('Obrigado! Volte sempre!')

print('\n\n <<<< MANIPULAÇÃO DE LISTAS >>>> \n')

lista  = [1,2,3,6,5,5,6]
print('\nLista ANTES da alteração : ', lista)

##############################################################
# >>>>>> 1) Para ADICIONAR em listas: <<<<<<
##############################################################

# append() - Adiciona UM dado no final da lista
lista.append(50)
print('append(50) > ', lista)
lista.append(4)
print('append(4) > ', lista)

# insert() - Precisa de um valor do indice, e do valor
lista.insert(0,'Texto')
print('\ninsert(Texto) > ', lista)
lista.insert(1, 7)
print('insert(1,7) > ', lista) 

# extend() - adiciona os elementos de uma lista à outra lista
lista.extend([4, 5, 6])
print('\nextend() > ', lista)
lista.extend([10,2,65,5,5,45,6,4,5])
print('extend() > ', lista)

# += - usado em  tuplas / listas (unico comando de manipulação de uma tupla)

lista += (10,2,5,6,6,4,5,5,5)
print('\n+= > ', lista)

##############################################################
# >>>>>> 2) Para REMOVER em listas: <<<<<<
##############################################################

# clear() - limpa todos os elementos da lista
lista.clear()
print('\nclear() > ', lista)

# pop() - remove e retorna o último elemento da lista
lista  = [7,[1,5],2,3,600,5,5,6]
elemento_removido = lista.pop()
print('\npop() > Elemento removido: ', elemento_removido)
print('pop() > ', lista)

# remove() - remove a primeira ocorrência de um elemento da lista
lista.remove(2)
print('\nremove(2) > ', lista)

# del - removerá o elemento da lista a partir de um índice
del lista[1][:]
lista[1] = 22
print('\ndel > ', lista)

##############################################################
# >>>>>> 3) Para VERIFICAR em listas: <<<<<<
# **Necessário que listas tenham somente 1 dimensão!
##############################################################

# sum() - soma todos os elementos da lista
soma = sum(lista)
print('\nsum() > ', soma)

# max() - retorna o valor máximo da lista
maximo = max(lista)
print('max() > ', maximo)

# min() - retorna o valor minimo da lista
minimo = min(lista)
print('min() > ', minimo)

# copy() - faz uma cópia da lista
copia = lista.copy()
print('copy() > ', copia)

# count() - conta a quantidade de ocorrências de um elemento na lista
quantidade = lista.count(5)
print('count(5) > ', quantidade)

# index() - retorna o índice do primeiro elemento encontrado na lista
indice = lista.index(3)
print('index(3) > ', indice)
print('index(600) > ', lista.index(600))

# sort() - ordena os elementos da lista (por padrão, em ordem crescente)
lista.sort()
print('sort(asc) > ', lista)

# sort() - ordenação em ordem decrescente
lista.sort(reverse=True)
print('sort(desc) > ', lista)

# split() - quebra uma string em palavras
M = 'Hello World!'
M = M.split()
print('\nsplit() > ', M)

# join() - realiza cruzamento entre tabelas
M = 'Hello World kdflsçkçsld'
delimiter = '-'
N = delimiter.join(M)
print('join() > ', N)

# range() - método de contagem de inicio, fim e steps em listas e loops
# range(start | stop | step by step)
range1 = list(range(0,11,2))
range2 = list(range(10))
range3 = list(range(1,31))
range4 = list(range(1,-2,-1))

print('\nrange() > ', range1)
print('range() > ', range2)
print('range() > ', range3)
print('range() > ', range4)

# EXERCÍCIOS

print('\n <<<< EXERCÍCIOS >>>> \n')

# **Exercício 0:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
print('Exercício 0: ')
for n in range(2,21,2):
    print(n) 

# **Exercício 1:** Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
numeros = list(range(1,11))
print('Exercício 1: ', numeros)

# **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.
terceiro = numeros[2]
print('Exercício 2: ', terceiro)

# **Exercício 3:** Adicione o número 9 à lista `numeros` e imprima a lista atualizada.
numeros.append(9)
print('Exercício 3: ', numeros)

# **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.
numeros.pop(4)
print('Exercício 4: ', numeros)

# **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.
carros = ['livina', 'gol', 'camaro']
lista_final = numeros + carros
print('Exercício 5: ', lista_final)

print('\n\n <<<< MANIPULAÇÃO DE TUPLAS >>>> \n')

# Principal diferença entre listas: IMUTABILIDADE (não deve ser alterada) 

# Podem ser usadas funções como:
    # append(), remove(), insert(), pop(), del()
    # sum(), max(), min(), len(), sort(), sorted(), count()

tupla = (1,2,3,6,9,45,1,14,4,'texto')

print(tupla[9])

l = list(tupla)
t = tuple(l)
print(t)
# x =  tuple(range(1,51))
# print(x)

a,c,b = [1,2,3]
print(a,c,b)


print('\n\n <<<< MANIPULAÇÃO DE CONJUNTOS >>>> \n')

# Criando um conjunto com chaves {}
conjunto1 = {1, 2, 3, 4, 66, 6, 6, 6}
print('\ncria com {} > ',conjunto1)

# Criando um conjunto com a função set()
conjunto2 = set({3, 4, 5, 6})
print('cria com set() > ',conjunto2)

##############################################################
# >>>>>> 1) Para ADICIONAR em conjuntos: <<<<<<
##############################################################

conjunto = {1, 2, 3}
conjunto.add(4)
print('\nadd(4) > ', conjunto)

##############################################################
# >>>>>> 2) Para REMOVER em conjuntos: <<<<<<
##############################################################

# Para remover um elemento de um conjunto, utilize os métodos remove() ou discard(). 
# A diferença entre eles é que remove() gera um erro se o elemento não estiver presente no conjunto, enquanto discard() não gera erro.

conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print('\nremove(3) > ', conjunto)

conjunto.discard(2)
print('discard(3) > ', conjunto)

conjunto.discard(5)  # Não gera erro se o elemento não existir
print('discard(5) > ', conjunto)

##############################################################
# >>>>>> 3) Para VERIFICAR em conjuntos: <<<<<<
##############################################################

# União
uniao = conjunto1 | conjunto2  # ou conjunto1.union(conjunto2)
print('\nunião > ', uniao)

# Interseção
intersecao = conjunto1 & conjunto2  # ou conjunto1.intersection(conjunto2)
print('intersecção > ', intersecao)

# Diferença
diferenca = conjunto1 - conjunto2  # ou conjunto1.difference(conjunto2)
print('diferença > ', diferenca)

# Diferença simétrica
dif_simetrica = conjunto1 ^ conjunto2  # ou conjunto1.symmetric_difference(conjunto2)
print('diferença simétrica > ', dif_simetrica)

# Verificar subconjunto
print({1, 2}.issubset(conjunto1))
print('subconjunto > ',conjunto1.issuperset({1, 2}))

print('\n\n <<<< MANIPULAÇÃO DE DICIONÁRIOS >>>> \n')

cadastro = {
    
    'Nome': [input('Seu nome: '), 'Fernando', 'Guilherme', 'Camila', 'Tania'],
    'Sobrenome': [input('Seu sobrenome: '), 'Sales', 'Xavier', 'Santos', 'Silva'],
    'Genero': [input('Seu gênero (M/F/Nao_se_aplica): '), 'M', 'Nao_se_aplica', 'F', 'F'],
    'Idade': [int(input('Sua idade: ')), 25, 31, 43, 62],
    'Estado': [input('Estado que reside (UF): '), 'SC', 'BA', 'SP', 'RJ'],
    'Endereco': [input('Seu endereço completo: '), 'Rua 45', 'Rua 10', 'Av 40', 'Av 75'],
    'Email': [input('Seu email: '), 'fernando@gmail.com', 'guilherme@gmail.com', 'camila@hotmail.com', 'tania@outlook.com'],
    'outros_dados': {
        'a': 10,
        'b': 20,
        'c': 30
    }
}

# print('\nLista de pessoas da base de dados: ', cadastro['Nome'])
cadastro['DDD'] = [int(input('Seu DDD: ')), '48', '61', '11', '21'],
cadastro['Telefone'] = [int(input('Seu Telefone Celular: ')), '987445874', '954781594', '965741285', '935741857'],
cadastro['Cor'] = [input('Sua cor favorita: '), 'preto', 'laranja', 'verde', 'azul']
cadastro['Esportes'] = [input('Seu esporte favorito: '), 'volei', 'futebol', 'tenis', 'nao_tem']
cadastro['Animal'] = [input('Seu animal doméstico favorito: '), 'nao_tem', 'cachorro', 'gato', 'papagaio']
cadastro['Prato'] = [input('Seu prato preferido: '), 'sushi', 'macarrao', 'pastel', 'pizza']
cadastro['Filhos'] = [input('Quantidade de filhos que tem: '), 'nao_tem', 'nao_tem', '1', '2']


print('\n>> Dados presentes no banco de dados: ')
print('\n', cadastro)
