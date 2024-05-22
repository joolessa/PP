import pygame
import sounddevice as sd
import numpy as np
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from tela_inicial import *
from obstaculos import *

def volume_microfone(duracao=0.05, fs=44100):
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    amplitude = np.max(np.abs(gravacao))
    return amplitude

def tela_de_jogo(tela):
    # funcao do jogo pra ajuste da velocidade
    tempo = pygame.time.Clock()

    # Carrega o arquivo assets.py
    assets = load_assets()

    # Para escrever o volume do microfone
    fonte = pygame.font.Font(None, 36)

    # Velocidade do personagem
    v_minion = 0 

    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites

    game = True
    minion = Minion(assets, 200, 200)
    piso = Piso(assets,650,height)
    teto = Teto(assets, 650,70)
    all_sprites.add(minion,piso,teto)

    while game:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        all_sprites.update()

        # Montagem de fundo e personagem
        tela.fill((0, 0, 0))
        tela.blit(assets['fundo'], (0,0))
        all_sprites.draw(tela)

        # Multiplicando por 20 para aumentar a sensibilidade do som
        volume = volume_microfone() * 20

        # Se o volume for maior que a sensibilidade do som o personagem sobe
        if volume > sensi_som:
            v_minion -= 0.5 * volume 
        # Se não ele cai com a gravidade
        else:
            v_minion += gravidade # Para cair mais rápido podemos aumentar a gravidade
        
        # Multiplicando a velocidade do personagem pelo amortecimento para ele parar de cair
        v_minion *= amortecimento
        minion.y += v_minion

        # ATENÇÃO: Não deixar o personagem sair da tela	
        if minion.bottom > tamanho_tela[1]:
            minion.bottom = tamanho_tela[1]
            v_minion = 0
        
        if minion.top < 0:
            minion.top = 0
            minion = 0

        pygame. display. update()
        
    pygame.quit()