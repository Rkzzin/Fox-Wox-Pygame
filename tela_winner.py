import pygame
import random
from os import path
from sprites import Botao
from config import *
from assets import *


def tela_winner(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando botoes
    botoes_gameover = pygame.sprite.Group()

    # Criando um botão apenas para pegar as medidas de um botão para realizar o cálculo
    medidas_botao = Botao(assets, '')

    # Criando 3 botões
    for i in range(3):
        if i == 0:
            botao_jogo = Botao(assets, "Jogar novamente")

            botao_jogo.rect.centerx = 3*LARG / 10
            botao_jogo.rect.centery = 1.5* ALT/3
            botoes_gameover.add(botao_jogo)

        if i == 1:
            botao_pontuacao = Botao(assets, "Pontuação")

            botao_pontuacao.rect.centerx = 7* LARG / 10
            botao_pontuacao.rect.centery = 1.5*ALT/3
            botoes_gameover.add(botao_pontuacao)

        else:
            botao_quit = Botao(assets, "VOLTAR AO MENU")

            botao_quit.rect.centerx = LARG / 2
            botao_quit.rect.centery = 6 * ALT / 8 
            botoes_gameover.add(botao_quit)
    
    running = True

    # Carrega música de fundo
    pygame.mixer.music.play(loops=-1)


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
                for btn in botoes_gameover:
                    if btn == botao_jogo:   # Se o botão de JOGO for clicado, vai para a tela do jogo
                        if btn.rect.collidepoint(event.pos):
                            state = GAME
                            running = False
                    if btn == botao_pontuacao:  # Se o botão de PONTUACAO for clicado, vai para a tela de pontuacao
                        if btn.rect.collidepoint(event.pos):  
                            state = PONTUACAO
                            running = False
                    if btn == botao_quit:  # Se o botão de QUIT for clicado, fecha o jogo
                        if btn.rect.collidepoint(event.pos):  
                            state = INIT
                            running = False

            # Cria animação quando o mouse passa em cima do botão
            if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão
                for btn in botoes_gameover:
                    if btn.rect.collidepoint(event.pos):
                        btn.mouse_over(True)
                    else:
                        btn.mouse_over(False)

        # Desenha o fundo
        screen.blit(assets[BACKGROUND], (0,0))
        botoes_gameover.draw(screen)

        # Escrevendo texto dos botões
        for btn in botoes_gameover:
            btn_texto = assets['font'].render(f"{btn.nome_do_jogo}", True, BRANCO)
            text_rect = btn_texto.get_rect()
            text_rect.centerx = btn.rect.centerx
            text_rect.centery = btn.rect.centery
            screen.blit(btn_texto, text_rect)

        # Escreve texto da tela
        tela_titulo = assets['font_media'].render("VOCÊ VENCEU!!", True, BRANCO)
        text_rect = tela_titulo.get_rect()
        text_rect.centerx = LARG / 4
        text_rect.centery = 150
        screen.blit(tela_titulo, text_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state