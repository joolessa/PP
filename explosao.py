import pygame
from pygame.sprite import Group
from assets import load_assets

# Código retirado do seguinte link: https://www.youtube.com/watch?v=d06aVDzOfV8
class Explosion(pygame.sprite.Sprite):
    def __init__(self, assets, center):
        pygame.sprite.Sprite.__init__(self)
        self.exp_anim = assets['exp_anim']
        self.image = self.exp_anim
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.exp_anim): 
                self.kill()
            else:
                center = self.rect.center
                self.image = self.exp_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center