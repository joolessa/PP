import pygame

# Iniciando Tela
pygame.init()
tela = pygame.display.set_mode((1300,800))
pygame.display.set_caption('PP GAME')
tempo = pygame.time.Clock()

# IMAGENS
fundo = pygame.Surface((1300,800))
fundo.fill('Yellow')

# LOOP PRINCIPAL
game = True
while game:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    tela.blit(fundo, (0,0))

    pygame.display.update()
    tempo.tick(60)

# FINALIZAÇÃO
pygame.quit()
