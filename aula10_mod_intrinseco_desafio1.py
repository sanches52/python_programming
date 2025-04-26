
# MAIN.PY

from funcoes import * 



def verificar():
    
    print('ESCOLA: ')

    frequencia  =  [10,9,8,1,0,5,8,9,10,0]
    print('media')
    media1 =  media(frequencia)
    print(media1)
    print('mediana')
    mediana1 = mediana(frequencia)
    print(mediana1)
    print('moda')
    moda1 = moda(frequencia)
    print(moda1)
    print('Desvio padrão')
    desvio1 = desvio(frequencia)
    print(desvio1)

    print('menor nota')
    menor_nota(frequencia)
    print('maior nota')
    maior_nota(frequencia)


verificar()

    
    ---------------
    
    FUNCOES.PY
    
    
import statistics


def moda(frequencia):
    moda1 = statistics.mode(frequencia)
    return moda1


def media(frequencia):
    media1 = statistics.mean(frequencia)
    return media1



def mediana(frequencia):
    mediana1 = statistics.median(frequencia)
    return mediana1


def menor_nota(frequencia):
    menor = min(frequencia)
    print(menor)

def maior_nota(frequencia):
    maior = max(frequencia)
    print(maior)


def desvio(frequencia):
    desvio1 = statistics.stdev(frequencia)
    return desvio1


-------------------------------------------------------

main2.py

from funcoes import * 



def verificar():

    empresa1 = [1000,6000,1200,8000,1400]
    empresa2 = [5000,4000,3000,2000,7000]
    empresa3 = [1200,1300,8000,3000,15000]
    empresa4 = [1400,1750,2000,4500,5900]

    print('Analise de salário: ')

    m =  media(empresa1)
    print('MÉDIA 1',m)

    m =  media(empresa2)
    print('MÉDIA 2',m)    

    m =  media(empresa3)
    print('MÉDIA 3',m)

    m =  media(empresa4)
    print('MÉDIA 4 ',m)

    print('***'*10)
    
    mo =  moda(empresa1)
    print('MODA 1',mo)

    mo =  moda(empresa2)
    print('MODA 2',mo)    

    mo =  moda(empresa3)
    print('MODA 3',mo)

    mo =  moda(empresa4)
    print('MODA 4 ',mo)

    print('***'*10)

    med =  mediana(empresa1)
    print('mediana 1',med)

    med =  mediana(empresa2)
    print('mediana 2',med)    

    med =  mediana(empresa3)
    print('mediana 3',med)

    med =  mediana(empresa4)
    print('mediana 4 ',mo)
   
    print('***'*10)

    desv = desvio(empresa1)
    print('desvio 1',desv)

    desv = desvio(empresa2)
    print('desvio 2',desv)    

    desv = desvio(empresa3)
    print('desvio 3',desv)

    desv = desvio(empresa4)
    print('desvio 4 ', desv)

verificar()    




