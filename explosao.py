import pygame
from pygame.sprite import _Group

class Explosao(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
