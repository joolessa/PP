import pygame
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from tela_inicial import *
from obstaculos import *

def tela_de_jogo(tela):

    # funcao do jogo pra ajuste da velocidade
    tempo = pygame.time.Clock()

    # Carrega o arquivo assets.py
    assets = load_assets()

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    game = True
    minion = Minion(assets, 200, 200)
    piso = Piso(assets,650,height)
    teto = Teto(assets, 650,70)
    all_sprites.add(minion,piso,teto)

    while game:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        all_sprites.update()

        tela.fill((0, 0, 0))

        tela.blit(assets['fundo'], (0,0))

        all_sprites.draw(tela)

        pygame. display. update()

    pygame.quit()