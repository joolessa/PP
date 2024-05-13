# BIBLIOTECAS
import pygame
import sounddevice as sd
import numpy as np

# DECLARAÇÃO DE VARIÁVEIS
tamanho_tela = (1300,800)
largura_personagem = 50
altura_personagem = 50

gravidade = 3 # Gravidade quanto maior o valor mais rapido o personagem cai
sensi_som = 1 # quanto o som precisa ser alto para o personagem subir
amortecimento = 0.95 # Amortecimento do som quanto maior o valor mais rapido o personagem para de cair
