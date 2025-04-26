#main.py 
      
from valores import valores_produtos
from pagamento import *
from finalizar import * 

# - FINALIZAR A COMPRA
# - SE DESPEDIR DO USUÁRIO   

def mercado():
    valores_produtos()
    lista_p = ['camisas', 'meias', 'shorts']
    lista_v = [5,3.2,4]

    carrinho = []
    m_valores = []

    # p1 = int(input('Digite o produto'))
    # p2 = int(input('Digite o produto'))
    # p3 = int(input('Digite o produto'))

    # carrinho.append(lista_p[p1])
    # carrinho.append(lista_p[p2])
    # carrinho.append(lista_p[p3])

    # m_valores.append(lista_v[p1])
    # m_valores.append(lista_v[p2])
    # m_valores.append(lista_v[p3])

    escolha  =  input('deseja pedir:')
    while escolha  == 's':
          p1 = int(input('Digite o produto'))
          carrinho.append(lista_p[p1])
          m_valores.append(lista_v[p1])
          escolha  =  input('deseja pedir:')


    me_p =  pag(m_valores)
    print('Seus produtos: ', carrinho)
    print(f'R$ {me_p}')
    print('---------- || --------------')
    forma =  forma_pag()
    print('Sua forma de pagamento é: ', forma)
    print('Obrigada volte sempre!')
    

mercado()

# -------------------------------------------

#finalizar.py

 def forma_pag():

    esc =  input('Escolha a forma de pagamento')
    
    return esc   

# -------------------------------------------

# pagamento

def pag(lista_valores):
    total = sum(lista_valores)
    return total

# -------------------------------------------

# valores
def valores_produtos():
    print('''
Camisas - R$ 5,00
Meias   - R$ 5,03
Shorts  - R$ 4,00
    
          
          ''')   