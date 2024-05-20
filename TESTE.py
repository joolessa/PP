import pygame
from personagem import *
from constantes import *
from assets import load_assets

tamanho_tela = (1300,800)
largura_personagem = 50
altura_personagem = 50

pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption ('PP')
tempo = pygame.time.Clock()

assets = load_assets()

all_sprites = pygame.sprite.Group()

game = True
minion = Minion(assets, 100, 100)
all_sprites.add(minion)

while game:

    tempo. tick(60)
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            game = False

    all_sprites.update()

    tela.fill((0, 0, 0))

    tela.blit(assets['fundo'], (0,0))
    tela.blit(assets['piso'], (0,height-100))
    tela.blit(assets['teto'], (0,130))

    all_sprites.draw(tela)

    pygame. display. update()

pygame.quit()