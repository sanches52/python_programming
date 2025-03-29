# DESAFIO
# Crie um e-commerce com a estrutura de dicionários.
# Produtos:  Livros, tablets e fones de ouvido

# As ações: 
    # Comprar()
    # Pagar()
    # Mostra o valor da compra


ecommerce ={

   'Livros': {
       'Tipos': ['Receitas', 'Romance', 'Didático', 'Atlas', 'Ficção'],
       'Valores':[200, 80, 150, 180, 100]
   },
   'Tablets': {
       'Marcas': ['Samsung', 'Apple', 'Positivo', 'LeNovo', 'LG'],
       'Valores':[3200, 4900, 2000, 1800, 2200]
   },
   'Fone_Ouvido': {
       'Marcas': ['Samsung', 'Apple', 'JBL', 'Xiaomi', 'Bose'],
       'Valores':[1000, 2500, 2000, 1200, 2700]
    }
}

financeiro ={

   'Forma_pgto': ['pix', 'cartao_debito', 'cartao_credito', 'boleto']
}

print('\n <<<<< Bem-vindo ao nosso E-Commerce! >>>>> ')
print(f'''
      
    Nossas categorias de produtos:
        1) Livros: 
            {ecommerce['Livros']['Tipos'][0]} - ${ecommerce['Livros']['Valores'][0]}
            {ecommerce['Livros']['Tipos'][1]} - ${ecommerce['Livros']['Valores'][1]}
            {ecommerce['Livros']['Tipos'][2]} - ${ecommerce['Livros']['Valores'][2]}
            {ecommerce['Livros']['Tipos'][3]} - ${ecommerce['Livros']['Valores'][3]}
            {ecommerce['Livros']['Tipos'][4]} - ${ecommerce['Livros']['Valores'][4]}

        2) Tablets:
            {ecommerce['Tablets']['Marcas'][0]} - ${ecommerce['Tablets']['Valores'][0]}
            {ecommerce['Tablets']['Marcas'][1]} - ${ecommerce['Tablets']['Valores'][1]}
            {ecommerce['Tablets']['Marcas'][2]} - ${ecommerce['Tablets']['Valores'][2]}
            {ecommerce['Tablets']['Marcas'][3]} - ${ecommerce['Tablets']['Valores'][3]}
            {ecommerce['Tablets']['Marcas'][4]} - ${ecommerce['Tablets']['Valores'][4]}
    
        3) Fone_Ouvido:
            {ecommerce['Fone_Ouvido']['Marcas'][0]} - ${ecommerce['Fone_Ouvido']['Valores'][0]}
            {ecommerce['Fone_Ouvido']['Marcas'][1]} - ${ecommerce['Fone_Ouvido']['Valores'][1]}
            {ecommerce['Fone_Ouvido']['Marcas'][2]} - ${ecommerce['Fone_Ouvido']['Valores'][2]}
            {ecommerce['Fone_Ouvido']['Marcas'][3]} - ${ecommerce['Fone_Ouvido']['Valores'][3]}
            {ecommerce['Fone_Ouvido']['Marcas'][4]} - ${ecommerce['Fone_Ouvido']['Valores'][4]}

    Nossas formas de pagamento: 
        {financeiro['Forma_pgto']}

''')

categoria = input('Qual categoria de produto voce escolhe? : ')
print(ecommerce[categoria])

valores = []
carrinho = []

escolha1 = input('Qual produto você escolhe? ')
escolha2 = input('Qual outro produto você escolhe? ')

carrinho.append(escolha1)
carrinho.append(escolha2)

valores.append(ecommerce[escolha1])
valores.append(ecommerce[escolha2])

soma = sum(valores)

print('Total', soma)









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