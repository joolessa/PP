import pygame
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from tela_inicial import *

def game_over(tela, fonte,tempo_duracao):
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    som_go = pygame.mixer.Sound('Sons/somgo.mp3')
    # Mostrar mensagem de game over
    mensagem = fonte.render("Game Over babes", True, vermelho)
    tela.blit(mensagem, (tela.get_width() // 2 - mensagem.get_width() // 2, tela.get_height() // 2 - mensagem.get_height() // 2))
    texto_score = fonte.render(f'Você soltou a voz por {tempo_duracao:.2f} segundos', True, branco)
    tela.blit(texto_score, (tela.get_width() // 2 - texto_score.get_width() // 2, tela.get_height() // 2 + texto_score.get_height()))
    som_go.play()
    pygame.display.update()
    pygame.time.wait(4000) 
    pygame.quit()
    exit() 