# MANIPULAÇÃO DOS EVENTOS
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO IVERIFIQUE, O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/

print('\n <<<< AULA 16 >>>> \n')

##############################################################
# >>>>>> JOGO PYGAME - LABIRINTO <<<<<<
############################################################## 

import pygame

# Inicializa o Pygame
pygame.init()

# define o tamanho da tela do jogo
largura, altura = 400, 400

# cria uma tela 400x400
tela = pygame.display.set_mode((largura, altura))

# definição do título do jogo       
pygame.display.set_caption("Labirinto")                     

# define cores a partir do código RGB
preto = (0, 0, 0)                                           
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# estabelece tamanho ede cada elemento do labirinto
tamanho_celula = 40

# matriz, definição dos espaçamentos no labirinto
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# posição no x e y | velocidade
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40

# função que desenha labirinto na tela considerando em formato de um retângulo
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


#loop que faz varredura se botão de fechar janela for pressionado. Se sim, finaliza programa
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Uso das arrows do teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

    # preenche a tela de branco
    tela.fill(branco)

    # desenha labirinto
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # atualiza um pedaço da tela do monitor com os movimentos
    pygame.display.flip()

    # taxa de atualização do jogo (FPS)
    pygame.time.Clock().tick(10)


pygame.quit()