import pygame
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from tela_inicial import *

def game_over(tela, fonte):
    # Mostrar mensagem de game over
    mensagem = fonte.render("Game Over", True, (255, 0, 0))
    tela.blit(mensagem, (tela.get_width() // 2 - mensagem.get_width() // 2, tela.get_height() // 2 - mensagem.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(3000)  # Espera 3 segundos antes de fechar
    pygame.quit()
    quit()