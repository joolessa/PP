import pygame

class Minion(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['minion']
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedx = 0
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx

