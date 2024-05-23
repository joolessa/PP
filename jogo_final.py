import pygame
import sounddevice as sd
import numpy as np
from personagem import Minion
from piso import Piso
from teto import Teto
from espinhos import Espinhos
from constantes import *
from assets import load_assets
from tela_inicial import *
from tela_final import game_over
from explosao import Explosao


# Função para resetar o jogo
def resetar_jogo():
    global jogador, todos_sprites
    jogador = Jogador()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)