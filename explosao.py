import pygame
from pygame.sprite import _Group

# Código retirado do seguinte link: https://www.youtube.com/watch?v=d06aVDzOfV8
class Explosao(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            image = pygame.image.load('Imagens/exp{}.png'.format(num))
            image = pygame.transform.scale(image, (100,100)) # Tamanho da explosão
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0

    def update(self):
        velocidade_explosao = 4
        self.counter += 1
        
        if self.counter >= velocidade_explosao and self.index < len(self.images)-1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images)-1 and self.counter >= velocidade_explosao:
            self.kill()
