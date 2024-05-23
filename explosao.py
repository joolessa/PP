import pygame
from pygame.sprite import Group
from assets import load_assets

class Explosao(pygame.sprite.Sprite):
    def __init__(self, assets, center):
        pygame.sprite.Sprite.__init__(self)
        self.exp_anim = assets['exp_anim']
        self.frame = 0
        self.image = self.exp_anim[self.frame]  
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame >= len(self.exp_anim):
                self.kill()
            else:
                self.image = self.exp_anim[self.frame]
                self.rect = self.image.get_rect(center=self.rect.center)
