import pygame
import random
from assets import *
from constantes import *

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('Imagens/obstaculo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura_obstaculo, largura_personagem))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width-largura_obstaculo)
        self.rect.y = random.randint(-100, -altura_obstaculo)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > height or self.rect.right < 0 or self.rect.left > width:
            self.rect.x = random.randint(0, width-largura_obstaculo)
            self.rect.y = random.randint(-100, -altura_obstaculo)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)