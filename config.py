from os import path

# Estabelece a pasta que contem as figuras e sons.
PERSONAGENS = path.join(path.dirname(__file__), 'assets', 'img', 'characters')
SONS = path.join(path.dirname(__file__), 'assets', 'snd')
FONTES = path.join(path.dirname(__file__), 'assets', 'fonte')
FUNDO = path.join(path.dirname(__file__), 'assets', 'img')
BOTAO = path.join(path.dirname(__file__), 'assets', 'img', 'botao')

TILES = path.join(path.dirname(__file__), 'assets', 'img', 'tiles')

# Dados gerais do jogo.
LARG = 1215                 # Largura da tela
ALT = 600                   # Altura da tela
FPS = 120                   # Frames por segundo
GRAVITY = 0.2               # Gravidade
VELO_X = 3.0                # Velocidade no eixo x
TILE_SIZE = 32              # Tamanho do tile (cada tile é um quadrado de 32x32 pixels)


# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)

# Define os tipos de tiles
CHAO_V = 1
CHAO_A = 2
FUNDO_ESCURO = 3
WATER = 4
BOLHAS = 5
GRAMA_FUNDO = 6
GRAMA_L = 7
GRAMA_R = 8
GRAMA_T = 9
GRAMA_TL = 10
GRAMA_TR = 11
CHAO_A_QD = 12
CHAO_A_QE = 13
CHAO_V_QD = 14
CHAO_V_QE = 15
DIREITINHA_A = 16
DIREITINHA_V = 17
ESQUERDINHA_A = 18
ESQUERDINHA_V = 19

# Define o mapa com os tipos de tiles
MAP = [
    [10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 11],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 13, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 14, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 13, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 14, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 13, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 14, 8],
    [2, 2, 2, 2, 2, 2, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 1, 1, 1, 1, 1, 1],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 13, 12, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 15, 14, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 12, 4, 4, 4, 4, 4, 4, 4, 4, 15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 16, 3, 3, 5, 3, 3, 3, 5, 3, 19, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]

# Estados para controle do fluxo da aplicação
INIT = 0
PLAYING = 1
GAME = 2
INSTRUCOES = 3
GAMEOVER = 4
PONTUACAO = 5
DONE = 6
NOME = 7