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

    # Para escrever o volume do microfone e o tempo da rodada
    fonte = pygame.font.Font(None, 36)
    # Início do tempo da rodada
    inicio_rodada = pygame.time.get_ticks()

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
        tela.fill(preto)
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
        minion.speed_y = v_minion 

        minion.update()

        # ATENÇÃO: Não deixar o personagem sair da tela	
        if minion.rect.bottom > tamanho_tela[1]:
            minion.rect.bottom = tamanho_tela[1]
            v_minion = 0
        
        if minion.rect.top < 0:
            minion.rect.top = 0
            v_minion = 0

        # Textos na tela
        duracao_rodada = (pygame.time.get_ticks() - inicio_rodada) / 1000
        texto_volume = fonte.render(f'Volume: {volume:.2f}', True, branco)
        texto_duracao = fonte.render(f'Tempo: {duracao_rodada:.2f}s', True, branco)
        # Desenhar o texto na tela
        tela.blit(texto_volume, (10, 10))
        tela.blit(texto_duracao, (10, 50))
        pygame. display. update()

    pygame.quit()

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('PP GAME')
tela_de_jogo(tela)