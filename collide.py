import pygame
import random
from assets import *
from constantes import *

# Função de colisão
def collide(minion, obstaculo):
    return minion.rect.colliderect(obstaculo.rect)

minion = Minion(assets, 200, 200)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpar a tela
    tamanho_tela.fill(branco)

    # Atualizar posição do segundo objeto para testar a colisão
    Ob.rect.x, object2.rect.y = pygame.mouse.get_pos()
    object2.rect.x -= object2.rect.width // 2
    object2.rect.y -= object2.rect.height // 2

    # Verificar colisão e imprimir o resultado
    if collide(object1, object2):
        print("Colisão detectada!")

    # Atualizar a tela
    pygame.display.flip()


# ----- Atualiza estado do jogo
# Atualizando a posição dos meteoros
load_assets.update()

# Verifica se houve colisão entre nave e meteoro
hits = pygame.sprite.spritecollide(, all_meteors, True)

# ----- Gera saídas
window.fill((0, 0, 0))  # Preenche com a cor branca
window.blit(background, (0, 0))
# Desenhando meteoros
all_sprites.draw(window)

pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit() 