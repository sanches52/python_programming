print('\n <<<< AULA 15 >>>> \n')

##############################################################
# >>>>>> PACOTE PYGAME <<<<<<
############################################################## 

# EXEMPLOS DE PACOTES:
    # 'beautifulsoup4' -  web
    # 'openpyxl’  -  trabalhar com excel

# ---------------**Manipulação de Dados:**---------------

    # 1. NumPy - Para computação numérica eficiente.
    # 2. pandas - Para manipulação e análise de dados tabulares.
    # 3. Matplotlib - Para criação de gráficos e visualização de dados.
    # 4. Seaborn - Para visualização de dados estatísticos.
    # 5. scikit-learn - Para aprendizado de máquina e aprendizado profundo.

# ---------------**Desenvolvimento Web:**---------------

    # 6. Flask - Para construir aplicativos web leves e rápidos.
    # 7. Django - Para desenvolvimento web completo e robusto.
    # 8. FastAPI - Para criação de APIs RESTful de maneira rápida e fácil.

# ---------------**Processamento de Texto e Linguagem Natural:**---------------

    # 9. NLTK (Natural Language Toolkit) - Para processamento de linguagem natural.
    # 10. spaCy - Uma biblioteca NLP moderna e eficiente.
    # 11. TextBlob - Para tarefas de processamento de texto, como análise de sentimentos.

# ---------------**Inteligência Artificial e Aprendizado de Máquina:**---------------

    # 12. TensorFlow - Uma biblioteca popular para aprendizado de máquina e aprendizado profundo.
    # 13. PyTorch - Uma estrutura de aprendizado profundo amplamente usada.
    # 14. Keras - Uma API de alto nível para construir redes neurais.
    # 15. OpenAI Gym - Para desenvolver e comparar algoritmos de aprendizado por reforço.

# ---------------**Manipulação de Imagem e Visão Computacional:**---------------

    # 16. OpenCV - Uma biblioteca de visão computacional para processamento de imagem.
    # 17. Pillow - Para manipulação de imagens (similar ao PIL - Python Imaging Library).

# ---------------**Manipulação de Datas e Horas:**---------------

    # 18. datetime - Biblioteca padrão para trabalhar com datas e horas.
    # 19. arrow - Uma biblioteca para manipulação de datas e horas mais amigável.

# ---------------**Bancos de Dados:**---------------

    # 20. SQLAlchemy - Para acesso e manipulação de bancos de dados relacionais.
    # 21. pymongo - Para interagir com bancos de dados MongoDB.
    # 22. SQLite - Biblioteca embutida para bancos de dados SQLite.

# ---------------**Redes e Comunicação:**---------------

    # 23. requests - Para fazer requisições HTTP.
    # 24. Twisted - Para programação de rede assíncrona.
    # 25. socket - Biblioteca padrão para programação de rede em baixo nível.

# ---------------**Interface Gráfica de Usuário (GUI):**---------------

    # 26. tkinter - Biblioteca padrão para criação de interfaces gráficas.
    # 27. PyQt e PySide - Bibliotecas para criação de interfaces gráficas com Qt.
    # 28. Kivy - Para criar aplicativos multiplataforma com interfaces sensíveis ao toque.

# ---------------**Outros:**---------------

    # 29. os - Biblioteca padrão para operações de sistema e arquivos.
    # 30. math - Biblioteca padrão para funções matemáticas.
    # 31. random - Biblioteca padrão para geração de números aleatórios.


#Pygame é uma biblioteca em Python usada para criar jogos e aplicações multimídia 

# Example file showing a basic pygame "game loop"
# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("dark blue")

#     # RENDER YOUR GAME HERE

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()

import pygame

pygame.init() #inicializa
tela = pygame.display.set_mode((500,500)) #tamanho da tela
pygame.display.set_caption('Titulo')

# Paleta de cores com valores hexadecimais e RGB: https://celke.com.br/artigo/tabela-de-cores-html-nome-hexadecimal-rgb
# Doc das funções: https://www.pygame.org/docs/ref/draw.html

run = True
while run == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
            quit()

        tela.fill('DarkOrchid')

        # Retângulo
        pygame.draw.rect(tela,('PeachPuff'),(215,300,70,170))
        # Polígono
        # pygame.draw.polygon(tela,('PeachPuff'), ((120, 120), (150, 120), (140, 130)), width=50)
        # Círculo
        pygame.draw.circle(tela,('PeachPuff'),(250, 250), 70)
        # Elipse
        pygame.draw.ellipse(tela,('PeachPuff'), (120,120,80,120))
        pygame.draw.ellipse(tela,('PeachPuff'), (300,120,80,120))

        pygame.display.flip()





