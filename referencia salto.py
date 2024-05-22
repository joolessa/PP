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
def volume_microfone(duracao=0.05, fs=44100):
    gravacao = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    amplitude = np.max(np.abs(gravacao))
    return amplitude

def atualizar_tela(tela, fonte, retangulo_personagem, volume):
    tela.fill((255, 255, 255))
    pygame.draw.rect(tela, (0, 0, 255), retangulo_personagem)
    texto_volume = fonte.render(f"Volume: {volume:.2f}", True, (0, 0, 0))
    retangulo_texto = texto_volume.get_rect()
    retangulo_texto.topright = (tamanho_tela[0] - 10, 10)
    tela.blit(texto_volume, retangulo_texto)
    pygame.display.update()




    
  
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
      
  #atualizar_tela(tela, fonte, minion, volume)
  relogio.tick(60)

  pygame.quit()