import pygame

class Minion(pygame.sprite.Sprite):
    def __init__(self, assets, x, y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['minion']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_y = 0  # Velocidade vertical

    def update(self):
        self.rect.y += self.self.speed_y