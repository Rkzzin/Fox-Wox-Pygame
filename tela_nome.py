import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *

def tela_nome(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando botoes
    botoes_nome = pygame.sprite.Group()

    # Calculando espaçamento entre os botões
    # Criando um botão apenas para pegar as medidas de um botão para realizar o cálculo
    medidas_botao = Botao(assets, '')

    '''
    O espaçamento é feito através da largura da janela menos o 
    espaço necessário para posicionar 4 botões
    depois é calculado o tamanho para 5 espaços vazios
    '''


    # Criando primeira fileira com 2 botões
    for i in range(1):
        botao_nome = Botao(assets, "NOME")

        botao_nome.rect.centerx = LARG / 2
        botao_nome.rect.centery = ALT / 2
        botoes_nome.add(botao_nome)

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in botoes_nome:
                    if btn == botao_nome:   # Se o botão de JOGO for clicado, vai para a tela do jogo
                        if btn.rect.collidepoint(event.pos):
                                state = GAMEOVER
                                running = False

            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for btn in botoes_nome:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)


        screen.blit(assets[BACKGROUND], (0,0))
        botoes_nome.draw(screen)

        # Escrevendo texto dos botões
        for btn in botoes_nome:
            btn_texto = assets['font'].render(f"{btn.nome_do_jogo}", True, BRANCO)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)

        tela_titulo = assets['font_media'].render("NOMEANDO JOGADOR:", True, BRANCO)
        text_rect = tela_titulo.get_rect()
        text_rect.centerx = LARG / 4
        text_rect.centery = 100
        screen.blit(tela_titulo, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state