import pygame
from constantes import *
from tela_jogo import *
from tela_inicial import tela_inicial
from tela_final import tela_final

pygame.init()
pygame.mixer.init()

# Gerar tela principal
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rinha de Bicho')

state = INICIAR
while state != FIM:
    
    if state == INICIAR: #leva até a tela de inicio
        state = tela_inicial(tela)
    if state == JOGO: # vai para tela do jogo
        state = tela_jogo(tela)
    if state == FINAL: #leva até a tela final
        state = tela_final(tela)  
    else:  
        state = FIM
    
    tela.fill((preto))

pygame.quit()