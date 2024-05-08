import pygame

# Iniciando Tela
pygame.init()
tela = pygame.display.set_mode((1152,800))
pygame.display.set_caption('PP GAME')
tempo = pygame.time.Clock()

# IMAGENS
imagem_inicial = pygame.image.load('/workspaces/PP/Imagens/fundo_inicial.jpeg')

# LOOP PRINCIPAL
game = True
while game:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game = False
    tela.blit(imagem_inicial, (0,0))

    pygame.display.update()
    tempo.tick(60)

# FINALIZAÇÃO
pygame.quit()
