print('\n <<<< AULA 12 >>>> \n')

##############################################################
# >>>>>> BLOCOS DE CÓDIGO <<<<<<
############################################################## 

# Estruturas de decisão:
    # If
    # If-else
    # If-elif-else
    # Laços de repetição (while / for)
    # for - range()

print('\n <<<< EXERCÍCIOS >>>> \n')

# ***Crie com módulos das funções utilize parâmetros/return:*** 

# **1 - Crie um número aleatório de 5,10**

import random

numero = random.randint(5,10)
print('Número aleatório: ', numero)

# **2 - Crie 3 números aleatórios**

n1, n2, n3 = random.randint(5,10), random.randint(5,10), random.randint(5,10)
print(n1,n2,n3)

# **3 - Crie um número aleatório entre 10 a 30. (use módulo range())**

numero2 =  random.randrange(10,30)
print(numero2)

# **4 - Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(use módulo for)

c  =  10
while c > 0:
    print(c)
    c = c - 1
print('fogo')  

# **5 - Soma de números pares**

# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# (use módulos if e for)

numero = int(input('inteiro: '))

soma = 0
for n in range(1,numero):
    if n % 2 == 0:
       soma =  soma +  n
print(soma) 


# **6 - Tabuada de multiplicação**

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (use módulos while ou for)

n1 = int(input('numero: '))

for x  in range(0,11):
    calculo =  n1 * x
    print(n1, 'X', x , '=', calculo)

c = 0
while c <= 10:
      calculo =  c * n1
      c = c + 1
      print(n1, 'X', c , '=', calculo)
      

# **7 -  Números ímpares reversos**

# Exiba uma contagem regressiva de números ímpares de 99 a 1.
# (use módulos for)

for m in range(99,0,-1):
    if m % 2 == 1:
        print(m)

# Lista avançada:
# m  =  [n for n in range(99,0,-1) if n % 2 == 1]
# print(m)

