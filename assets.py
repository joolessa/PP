import pygame
from constantes import *

def load_assets():
    assets = {}

    assets['minion'] = pygame.transform.scale(pygame.image.load('Imagens/minion.png').convert_alpha(), (largura_personagem, altura_personagem))
    assets['fundo'] = pygame.image.load('Imagens/Fundo.png')
    assets['piso'] = pygame.image.load('Imagens/piso.PNG')
    assets['teto'] = pygame.image.load('Imagens/teto.PNG')
    assets['espinhos'] = pygame.image.load('Imagens/obstaculo.png')
    assets['exp1'] = pygame.image.load('Imagens/exp1.png')
    assets['exp2'] = pygame.image.load('Imagens/exp2.png')
    assets['exp3'] = pygame.image.load('Imagens/exp3.png')
    assets['exp4'] = pygame.image.load('Imagens/exp4.png')
    assets['exp5'] = pygame.image.load('Imagens/exp5.png')
    exp_anim = [assets['exp1'],assets['exp2'], assets['exp3'], assets['exp4'], assets['exp5']]

    return (assets, exp_anim)