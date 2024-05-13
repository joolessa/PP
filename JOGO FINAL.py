# BIBLIOTECAS
import pygame
import sounddevice as sd
import numpy as np

# DECLARAÇÃO DE VARIÁVEIS
tamanho_tela = (1300,800)
largura_personagem = 70
altura_personagem = 70
# Dados que podem ser ajustados em caso de delay
gravidade = 3 # gravidade quanto maior o valor mais rapido o personagem cai
sensi_som = 1 # quanto o som precisa ser alto para o personagem subir
amortecimento = 0.95 # amortecimento do som quanto maior o valor mais rapido o personagem para de cair

# FUNÇÕES
#
#
#

# EXECUÇÃO DO JOGO
pygame.init()
janela = pygame.display.set_mode(tamanho_tela)
imagem_fundo = pygame.image.load('/workspaces/PP/Imagens/Fundo.png')
pygame.display.set_caption('PP Game')

relogio = pygame.time.Clock()
fonte = pygame.font.Font(None, 36) # Para escrever o volume do microfone

minion = pygame.image.load("/workspaces/PP/Imagens/Minion Bob.png")
v_minion = 0

# LOOP PRINCIPAL
game = True
while game:
  # Fechamento do jogo
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      game = False
  
  # Montagem de fundo e personagem
  janela.blit(imagem_fundo, (0,0))
  janela.blit(minion, (tamanho_tela[0] // 4, tamanho_tela[1] - altura_personagem, largura_personagem, altura_personagem))
        
  # Multiplicando por 20 para aumentar a sensibilidade do som
   #  volume = volume_microfone() * 20
  
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
    if minion.bottom > tamanho_telaminion[1]:
      minion.bottom = tamanho_telaminion[1]
      v_minion = 0
        
    if minion.top < 0:
      minion.top = 0
      minion = 0
      
    #atualizar_tela(tela, fonte, minion, volume)
    relogio.tick(60)

    pygame.quit()
