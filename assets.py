import pygame
from constantes import *

def load_assets():
    assets = {}

    assets['minion'] = pygame.transform.scale(pygame.image.load('Imagens/minion.png').convert_alpha(), (largura_personagem, altura_personagem))
    assets['fundo'] = pygame.image.load('Imagens/Fundo.png')
    assets['piso'] = pygame.image.load('Imagens/piso.PNG')
    assets['teto'] = pygame.image.load('Imagens/teto.PNG')
    assets['espinhos'] = pygame.image.load('Imagens/obstaculo.png')
    assets['exp_anim'] = [
    pygame.image.load('Imagens/exp1.png'),
    pygame.image.load('Imagens/exp2.png'),
    pygame.image.load('Imagens/exp3.png'),
    pygame.image.load('Imagens/exp4.png'),
    pygame.image.load('Imagens/exp5.png')]
       
    scale_factor = 2  # Adjust scale factor as needed for desired size
    assets['explosion_frames'] = [pygame.transform.scale(pygame.image.load(f'Imagens/{img}').convert_alpha(), (int(width * scale_factor), int(height * scale_factor))) for img in assets['exp_anim']]
    return assets