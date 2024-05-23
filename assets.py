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

    # Código gerado por https://chatgpt.com/?model=gpt-4 
    explosion_images = ['exp1.png', 'exp2.png', 'exp3.png', 'exp4.png', 'exp5.png']
    scale_factor = 2  # Scale factor to increase the size of the explosion images

    assets['explosion_frames'] = [pygame.transform.scale(pygame.image.load(f'Imagens/{img}').convert_alpha(), 
                                  (int(80 * scale_factor), int(80 * scale_factor))) for img in explosion_images]
    return assets