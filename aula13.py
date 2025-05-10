print('\n <<<< AULA 13 >>>> \n')

##############################################################
# >>>>>> MANIPULAÇÃO DE DIRETÓRIOS <<<<<<
############################################################## 

print('\n <<<< EXERCÍCIOS >>>> \n')

import os
import shutil

# 1: Criar e ler um Arquivo

with open('arquivo_teste.txt', 'w') as f:
    f.write('Este é um arquivo de teste.')

# Ler o arquivo
with open('arquivo_teste.txt', 'r') as f:
    conteudo = f.read()
    print(conteudo)

# 2: Cria um Diretório

diretorio = 'meu_diretorio'
os.makedirs(diretorio, exist_ok=True)  
os.chdir(diretorio) 
print('Diretório atual:', os.getcwd())


# 3: Renomear um Diretório

os.chdir('c:/Users/Aluno/Desktop/Aluno')
os.rename('meu_diretorio', 'diretorio_renomeado')
print('Diretórios após renomear:', os.listdir())

# 4:  Listar Arquivos em um Diretório

arquivos = os.listdir()
print('Arquivos no diretório atual:', arquivos)

# 5:  Copiar Arquivos em um Diretório

os.makedirs('backup', exist_ok=True)

shutil.copy('arquivo_teste.txt', 'backup/arquivo_teste_copia.txt')
print('Arquivos no diretório backup:', os.listdir('backup'))

# 6: Copiar Arquivos em um Diretório

shutil.rmtree('diretorio_renomeado')
print('Diretórios após remoção:', os.listdir())