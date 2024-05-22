import pygame
import random
from constantes import *

class Espinhos(pygame.sprite.Sprite):
    def __init__(self, assets):
        super().__init__()
        self.image = pygame.transform.scale(assets['espinhos'], (80, 80))
        self.rect = self.image.get_rect()

        # Aparecendo no canto direito da tela, em uma posição vertical aleatória
        self.rect.x = tamanho_tela[0]
        self.rect.y = random.randint(0, tamanho_tela[1] - self.rect.height)

        # Velocidade inicial dos espinhos
        self.speed = 20

    def update(self):
        self.rect.x -= self.speed  # Movimento horizontal para a esquerda
        if self.rect.right < 0:  # Se o espinho sair da tela pela esquerda, ele é removido
            self.kill()
