import pygame
import sounddevice as sd
import numpy as np
import random
import math
from personagem import *
from piso import *
from teto import *
from constantes import *
from assets import load_assets
from obstaculos import *
from tela_final import game_over
from microfone import volume_microfone

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
    espinhos_group = pygame.sprite.Group()

    game = True
    minion = Minion(assets, 200, 200)
    piso = Piso(assets,650,height)
    teto = Teto(assets, 650,70)
    all_sprites.add(minion,piso,teto)

    tempo_jogo = 0
    velocidade_espinhos = 5  # Velocidade inicial dos espinhos

    # Função para adicionar espinhos
    def adicionar_espinhos():
        espinho = Espinhos(assets, minion)
        espinho.speed = velocidade_espinhos  
        espinho.calculate_trajectory()  
        all_sprites.add(espinho)
        espinhos_group.add(espinho)

    # Adicionar espinhos periodicamente
    adicionar_espinhos_event = pygame.USEREVENT + 1
    pygame.time.set_timer(adicionar_espinhos_event, 2000)

    while game:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        all_sprites.update()

        if not minion.alive:
            game_over(tela, fonte)

        # Montagem de fundo e personagem
        tela.fill(preto)
        tela.blit(assets['fundo'], (0,0))
        all_sprites.draw(tela)

        # aumentar a sensibilidade do som
        volume = volume_microfone() * 1500

       
        # Se o volume for maior que a sensibilidade do som o personagem sobe
        if volume > sensi_som:
            v_minion -= 3 * volume 
        # Se não ele cai com a gravidade
        else:
            v_minion += gravidade # Para cair mais rápido podemos aumentar a gravidade
        
        # Multiplicando a velocidade do personagem pelo amortecimento para ele parar de cair
        v_minion *= amortecimento
        minion.rect.y += v_minion 

        minion.update()
       
        # ATENÇÃO: Não deixar o personagem sair da tela	
        if minion.rect.bottom > tamanho_tela[1]:
            minion.rect.bottom = tamanho_tela[1]
            v_minion = 0
        
        if minion.rect.top < 0:
            minion.rect.top = 0
            v_minion = 0

        # Aumenta a dificuldade do jogo
        tempo_jogo += 1
        if tempo_jogo % 600 == 0:  # A cada 10 segundos aumenta a velocidade dos espinhos
            velocidade_espinhos += 1
            print(f'Nova velocidade dos espinhos: {velocidade_espinhos}')

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