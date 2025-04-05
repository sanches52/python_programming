# DESAFIO

# Crie um e-commerce com a estrutura de dicionários.
# Produtos:  Livros, tablets e fones de ouvido
# As ações: 
    # Comprar()
    # Pagar()
    # Mostra o valor da compra


ecommerce = {

   'Livros': {
       'Receitas': {
            'Palmirinha': 200.00
       },
       'Romance': {
            'Protegendo o Perigo': 80.00,
            'Orgulho e Preconceito': 70.00
       },
       'Didáticos': {
            'Aurélio': 150.00,
            'Oxford': 180.00,
            'Cambridge': 2000.00
       },
       'Atlas': {
            'Américas': 130.00,
            'África': 190.00,
            'Ásia': 140.00
       },
       'Ficção': {
            'O Guia do Mochileiro das Galáxias': 100.00,
            '1984': 120.00
       }
   },
   'Tablets': {
        'Samsung': {
            'Galaxy Tab A9': 2900.00,
            'Galaxy Tab S6 Lite': 3200.00,
            'Galaxy Tab S9 Ultra': 5200.00,
            'Galaxy Tab S10 Ultra': 7900.00
       },
       'Apple': {
            'iPad Air': 4900.00,
            'iPad Mini': 5900.00,
            'iPad Pro': 7900.00
       },
       'Positivo': {
            'Vision Tab 7': 2000.00,
            'Vision Tab 7 Stitch': 3500.00,
            'Vision Tab 10': 6700.00
       },
       'LeNovo': {
            'Tab M9': 3400.00,
            'Tab P12': 4900.00,
            'Ásia': 140.00
       },
       'LG': {
            'G Pad': 2600.00
       }
   },
   'Fone_Ouvido': {
        'Samsung': {
            'Galaxy Buds Pro': 1000.00,
            'Galaxy Bud Live': 1600.00,
            'Galaxy Buds 2': 800.00
       },
       'Apple': {
            'AirPods 2': 1800.00,
            'AirPods 2': 2200.00,
            'AirPods Pro': 3800.00
       },
       'JBL': {
            'Wave Buds': 700.00,
            'Live Beam 3': 1400.00,
            'Wave Flex': 900.00
       },
       'Xiaomi': {
            'Redmi Buds 4 Pro': 400.00,
            'Redmi Buds 5 Pro': 600.00,
            'Redmi Buds 6 Active': 1100.00
       },
       'Bose': {
            'QuietComfort 35 II': 3000.00,
            'QuietComfort Ultra': 4200.00
       }
    }
}

financeiro ={

   'Forma_pgto': ['pix', 'cartao_debito', 'cartao_credito', 'boleto']
}

print('\n <<<<< Bem-vindo ao nosso E-Commerce! >>>>> ')
print(f'''
      
    Nossas categorias de produtos:
        1) Livros: 
            {ecommerce['Livros']['Receitas']} -
            
''')

#             {ecommerce['Livros']['Receitas']} - ${ecommerce.keys(['Livros']['Receitas'])}

#             {ecommerce['Livros']['Romance'][1]} - ${ecommerce['Livros']['Valores'][1]}
#             {ecommerce['Livros']['Didáticos'][2]} - ${ecommerce['Livros']['Valores'][2]}
#             {ecommerce['Livros']['Atlas'][3]} - ${ecommerce['Livros']['Valores'][3]}
#             {ecommerce['Livros']['Ficção'][4]} - ${ecommerce['Livros']['Valores'][4]}



#         2) Tablets:
#             {ecommerce['Tablets']['Marcas'][0]} - ${ecommerce['Tablets']['Valores'][0]}
#             {ecommerce['Tablets']['Marcas'][1]} - ${ecommerce['Tablets']['Valores'][1]}
#             {ecommerce['Tablets']['Marcas'][2]} - ${ecommerce['Tablets']['Valores'][2]}
#             {ecommerce['Tablets']['Marcas'][3]} - ${ecommerce['Tablets']['Valores'][3]}
#             {ecommerce['Tablets']['Marcas'][4]} - ${ecommerce['Tablets']['Valores'][4]}
    
#         3) Fone_Ouvido:
#             {ecommerce['Fone_Ouvido']['Marcas'][0]} - ${ecommerce['Fone_Ouvido']['Valores'][0]}
#             {ecommerce['Fone_Ouvido']['Marcas'][1]} - ${ecommerce['Fone_Ouvido']['Valores'][1]}
#             {ecommerce['Fone_Ouvido']['Marcas'][2]} - ${ecommerce['Fone_Ouvido']['Valores'][2]}
#             {ecommerce['Fone_Ouvido']['Marcas'][3]} - ${ecommerce['Fone_Ouvido']['Valores'][3]}
#             {ecommerce['Fone_Ouvido']['Marcas'][4]} - ${ecommerce['Fone_Ouvido']['Valores'][4]}

#     Nossas formas de pagamento: 
#         {financeiro['Forma_pgto']}

# >>>> ETAPA COMPRAR()
categoria = input('Qual categoria de produto voce escolhe? : ')
print(ecommerce[categoria])

valores = []
carrinho = []

escolha1 = input('Qual produto você escolhe? ')
escolha2 = input('Qual outro produto você escolhe? ')

carrinho.append(escolha1)
carrinho.append(escolha2)
# OU carrinho += (escolha1, escolha2)

valores.append(ecommerce[escolha1])
valores.append(ecommerce[escolha2])
# OU valores = [ecommerce[produto1], ecommerce[produto2]]

print('Os produtos escolhidos foram: ', carrinho)

total_compra = sum(valores)

# Mostra o valor total da compra
print('Total', total_compra)

# >>>> ETAPA PAGAR()

print('''Escolha uma forma de pagamento
        1 - PIX
        2 - Cartão de Crédito
        3 - Cartão de Débito
        ''')
        
pag = ['', 'pix','cc', 'cd']


escolha_pagamento = int(input('>>')) 


print('Forma de pagamento:', pag[escolha_pagamento])


print('Obrigada Volte Sempre!')





# print(ecommerce['formas_pag'][0])

# escolha1 = input('Digite o nome do produto') 
# print(ecommerce[escolha1])

# ecommerce = {

#     'fones':200,
#     'computadores':500
# }

# 1 comprar
# carrinho = []
# valores  =  []
# escolha_produto1 = input('escolha produto _ fones, computadores')
# tipo_produto1 = int(input('Escolha tipo x, n, r '))
# escolha_produto2 = input('escolha produto _ fones, computadores')
# tipo_produto2 = int(input('Escolha tipo x, n, r