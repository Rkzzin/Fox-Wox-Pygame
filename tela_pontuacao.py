import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *
from tela_jogo import *

pontuados = {}

def tela_pontuacao(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYDOWN:
                state = GAMEOVER
                running = False
            
        screen.blit(assets[BACKGROUND], (0,0))

        nome = assets['font_media'].render("NOME: ", True, BRANCO)
        text_rect = nome.get_rect()
        text_rect.x = 50
        text_rect.centery = 50
        screen.blit(nome, text_rect)

        pontuacao = assets['font_media'].render("TEMPO:", True, BRANCO)
        text_rect = pontuacao.get_rect()
        text_rect.centerx = (LARG / 2) + 100
        text_rect.centery = 50
        screen.blit(pontuacao, text_rect)

        dados = assets
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state