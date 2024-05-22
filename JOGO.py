import pygame
import sounddevice as sd
import numpy as np
import random
from personagem import Minion
from piso import Piso
from teto import Teto
from espinhos import Espinhos
from constantes import *
from assets import load_assets
from tela_inicial import *
from tela_final import game_over

def volume_microfone(duracao=0.05, fs=44100):
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    amplitude = np.max(np.abs(gravacao))
    print(f'Amplitude Capturada: {amplitude}')  # DEBBUG
    return amplitude

def tela_de_jogo(tela):
    game = True # variável para o loop principal
    assets = load_assets() # carrega os assts do assets.py

    # Para escrever o volume do microfone e o tempo da rodada
    pygame.font.init() # inicialização de fonte para os textos de tela
    fonte = pygame.font.Font(None, 36)
    
    # Início do tempo da rodada
    tempo = pygame.time.Clock() # tempo de jogo
    inicio_rodada = pygame.time.get_ticks()
    tempo_jogo = 0

    # Adicionando Sprites (minion, piso, teto e espinhos)
    all_sprites = pygame.sprite.Group()
    espinhos_group = pygame.sprite.Group()
    # dimensões
    minion = Minion(assets, 200, 200)
    piso = Piso(assets, 650, height)
    teto = Teto(assets, 650, 70)
    all_sprites.add(minion, piso, teto)
    # velocidades
    v_minion = 0 # velocidade inicial do minion 
    velocidade_espinhos = 100  # velocidade inicial dos espinhos 

    # Função para adicionar espinhos
    def adicionar_espinhos():
        espinho = Espinhos(assets)
        espinho.speed = velocidade_espinhos
        all_sprites.add(espinho)
        espinhos_group.add(espinho)
        print("Espinho adicionado") #DEBBUG
 
    # Código gerado por https://chatgpt.com/?model=gpt-4
    adicionar_espinhos_event = pygame.USEREVENT + 1
    pygame.time.set_timer(adicionar_espinhos_event, 2000) # adiciona espinhos na tela de 2 em 2 segundos

    # LOOPING PRINCIPAL
    while game:
        tempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == adicionar_espinhos_event:
                if not espinhos_group: # queremos só um espinho por vez na tela
                    adicionar_espinhos()

        all_sprites.update()
        espinhos_group.update()

        # Collided
        if pygame.sprite.spritecollide(minion, espinhos_group, False) or pygame.sprite.collide_rect(minion, piso) or pygame.sprite.collide_rect(minion, teto):
            game_over(tela, fonte,duracao_rodada)

        # Montagem de fundo e personagem
        tela.fill(preto)
        tela.blit(assets['fundo'], (0, 0))
        all_sprites.draw(tela)

        # Ajuste da sensibilidade do som
        volume = volume_microfone() * 3000
        print(f'Volume Capturado: {volume}') # DEBBUG

        # Se o volume for maior que a sensibilidade do som o personagem sobe
        if volume > sensi_som:
            v_minion -= 3 * volume 
        # Se não ele cai com a gravidade
        else:
            v_minion += gravidade
        
        # Multiplicando a velocidade do personagem pelo amortecimento para ele parar de cair
        v_minion *= amortecimento
        minion.rect.y += v_minion 
        print(f'v_minion: {v_minion}, minion.rect.y: {minion.rect.y}') # DEBBUG

        # ATENÇÃO: Não deixar o personagem sair da tela    
        if minion.rect.bottom > tamanho_tela[1]:
            minion.rect.bottom = tamanho_tela[1]
            v_minion = 0
        if minion.rect.top < 0:
            minion.rect.top = 0
            v_minion = 0

        # Aumentar a dificuldade do jogo
        tempo_jogo += 1
        if tempo_jogo % 600 == 0:  # A cada 10 segundos aumenta a velocidade dos espinhos
            velocidade_espinhos += 1
            print(f'Nova velocidade dos espinhos: {velocidade_espinhos}')

        # Textos na tela
        duracao_rodada = (pygame.time.get_ticks() - inicio_rodada) / 1000
        texto_volume = fonte.render(f'Volume: {volume:.2f}', True, branco)
        texto_duracao = fonte.render(f'Tempo: {duracao_rodada:.2f}s', True, branco)
        tela.blit(texto_volume, (10, 10))
        tela.blit(texto_duracao, (10, 50))
        pygame.display.update()

    pygame.quit()

# Inicialização do Pygame e variáveis de tela
pygame.init()
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('PP GAME')
tela_de_jogo(tela)