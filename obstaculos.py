import pygame
import random
import math
from constantes import *

class Espinhos(pygame.sprite.Sprite):
    # velocidade do triangulo
    def _init_(self, assets,minion):
        super()._init_()
        self.image = assets['espinhos']
        self.rect = self.image.get_rect()
        self.minion = minion

        self.rect.x = random.randint(0, tamanho_tela[0])
        self.rect.y = 0

        self.speed = 5
        self.calculate_trajectory()

    def calculate_trajectory(self):
        dx = self.minion.rect.x - self.rect.x
        dy = self.minion.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1
        self.velocity_x = self.speed * (dx / dist)
        self.velocity_y = self.speed * (dy / dist)
    
    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.colliderect(self.minion.rect):
            self.minion.alive = False
            self.kill() 