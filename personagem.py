import pygame

class Minion(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        super().__init__()
        self.image = assets['minion']  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 0  
        
    def update(self):
        self.rect.y += self.speed_y