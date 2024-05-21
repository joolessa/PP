import pygame
import random
from assets import *
from constantes import *

class Obstaculo(pygame.sprite.Sprite):
    # velocidade do triangulo
    def _init_(self, speed):
        super()._init_()  #inicialização correta
        self.image = pygame.transform.scale(pygame.image.load('Imagens/obstaculo.png'), (50, 50))  # imagem do obstáculo
        # 'x' é largura da tela (começando fora dela), e 'y' uma posição aleatória 
        self.rect = self.image.get_rect(x=width, y=random.randint(50, height - 50))
        self.speed = speed  # velocidade do obstáculo
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()