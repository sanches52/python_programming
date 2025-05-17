print('\n <<<< AULA 16 >>>> \n')

##############################################################
# >>>>>> JOGO PYGAME - PING-PONG <<<<<<
############################################################## 

import pygame

pygame.init()
janela =  pygame.display.set_mode([500,500])

BRANCO = (255,255,255) 
PRETO = (0,0,0)

# posição
raquete1_x, raquete1_y = 50, 225
raquete2_x, raquete2_y = 450,225
bola_x,bola_y = 250,250

velocidade_raquete = 0.5
velocidade_bola_x, velocidade_bola_y = 0.1, 0.1

raquete_largura, raquete_altura = 20,100
bola_largura, bola_altura = 20,20

placar1 = 0
placar2 = 0

font = pygame.font.SysFont(None,55)

def desenhar():
    janela.fill(BRANCO)
    pygame.draw.rect(janela, PRETO,(raquete1_x,raquete1_y,raquete_largura,raquete_altura))
    pygame.draw.rect(janela, PRETO, (raquete2_x,raquete2_y,raquete_largura,raquete_altura))
    pygame.draw.ellipse(janela,PRETO, (bola_x,bola_y,bola_largura, bola_altura))
    
    placar_texto = font.render(f'{placar1} | {placar2}', True, PRETO)

    janela.blit(placar_texto, (200,20))

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    keys = pygame.key.get_pressed()

# raquete 1
    if keys[pygame.K_w] and raquete1_y > 0:
        raquete1_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete1_y < 500 - raquete_altura:
        raquete1_y += velocidade_raquete

# raquete 2
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - raquete_altura:
        raquete2_y += velocidade_raquete

# velocidade da bola 
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

# impedir a bola de sair da tela 
    if bola_y <= 0 or bola_y >= 498 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y
    

# colisão 
    if (raquete1_x < bola_x < raquete1_x + raquete_largura) and (raquete1_y < bola_y <raquete1_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x
        
    if (raquete2_x < bola_x < raquete2_x + raquete_largura) and (raquete2_y < bola_y <raquete2_y + raquete_altura):
        velocidade_bola_x = -velocidade_bola_x

    if bola_x <=0: 
        placar2 += 1
        bola_x,bola_y = 250,250

    if bola_x >= 500: 
        placar1 += 1
        bola_x,bola_y = 250,250    

    desenhar()

    pygame.display.update()

