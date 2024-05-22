import pygame
import random
import math
from constantes import *
from assets import load_assets

class Espinhos(pygame.sprite.Sprite):
    # velocidade do triangulo
    def _init_(self, assets):
        super()._init_()
        self.image = assets['espinhos']
        self.rect = self.image.get_rect()

        self.rect.x = tamanho_tela[0]
        self.rect.y = random.randint(0, tamanho_tela[1] - self.rect.height)

        self.speed = 5

    def update(self):
        self.rect.x -= self.speed  # Movimento horizontal para a esquerda
        if self.rect.right < 0: 
            self.kill()