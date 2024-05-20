import pygame
from constantes import *

def load_assets():
    assets = {}

    assets['minion'] = pygame.transform.scale(pygame.image.load('Imagens/minion.png').convert_alpha(), (largura_personagem, altura_personagem))
    assets['fundo'] = pygame.image.load('Imagens/Fundo.png')
    assets['piso'] = pygame.image.load('Imagens/piso.PNG')
    assets['teto'] = pygame.image.load('Imagens/teto.PNG')
    
    return assets