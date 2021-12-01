
import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.05)
pygame.mixer.music.play(-1)

x_rect = 0
y_rect = 0

x_circle = randint(20, 620)
y_circle = randint(20, 400)

pontos = 6

fonte = pygame.font.SysFont('arial', 25, bold=True, italic=True)

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Nosso joguinho Breakout')
relogio = pygame.time.Clock()
morreu = False


def reiniciar_jogo():
    global pontos, x_rect, y_rect, x_circle, y_circle, morreu
    pontos = 0
    x_rect = 0
    y_rect = 0
    x_circle = randint(20, 620)
    y_circle = randint(20, 400)
    morreu = False


while True:
    relogio.tick(100)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if pygame.key.get_pressed()[K_a]:
        x_rect = x_rect - 20
        if x_rect < 0:
            x_rect = 0
    if pygame.key.get_pressed()[K_d]:
        x_rect = x_rect + 20
        if x_rect > 580:
            x_rect = 580
   
    rect = pygame.draw.rect(tela, (0, 255, 0), (x_rect, 400, 60, 10))
    circle = pygame.draw.circle(tela, (0, 0, 0), (x_circle, y_circle), 5)

    if rect.colliderect(circle):
        x_circle = randint(20, 620)
        y_circle = randint(20, 400)
        pontos = pontos + 1
        barulho_colisao.play()
        if x_circle < 0:
            x_circle = 0
        if x_circle > 635:
            x_circle = 635
        if y_circle < 0:
            y_circle = 0
        if y_circle > 400:
            fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    


    tela.blit(texto_formatado, (500, 20))

    pygame.display.update()
