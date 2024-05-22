import pygame
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from tela_inicial import *

def tela_final(tela, tempo_duracao, fonte):
    # Mostrar mensagem de game over
    mensagem = fonte.render("PP Game Over", True, branco)
    # texto mostrando o tempo o jogador ficou vivo
    texto_score = fonte.render(f'Você soltou a voz por {tempo_duracao:.2f} segundos', True, branco)
    pos_texto1 = texto_score.get_rect(center=((width// 2), (height // 2)-100))
    pygame.display.update()
    pygame.time.wait(3000)  # Espera 3 segundos antes de fechar
    pygame.quit()
    quit()