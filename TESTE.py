import pygame

tamanho_tela = (1300,800)

pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption ('PP')
tempo = pygame.time.Clock()

fundo = pygame.image.load('Imagens/Fundo.png')
piso = pygame.image.load('Imagens/piso.PNG')
teto = pygame.image.load('Imagens/teto.PNG')
minion = pygame.image.load('Imagens/teto.PNG')

game= True
while game:
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            game = False

    tela.blit(fundo, (0,0))
    tela.blit(piso, (0,700))
    tela.blit(teto, (0,700))

    pygame. display. update()
    tempo. tick(60)

pygame.quit()