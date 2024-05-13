import pygame

tamanho_tela = (1300,800)
largura_personagem = 50
altura_personagem = 50

pygame.init()
janela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('PP Game')

imagem_fundo = pygame.image.load('/workspaces/PP/Imagens/Fundo.png')
minion = pygame.image.load("/workspaces/PP/Imagens/Minion Bob.png")

game = True
while game:
    for evento in pygame.event.get():
        if evento == pygame.QUIT:
            game = False
    
    janela.blit(imagem_fundo, (0,0))
    janela.blit(minion, (tamanho_tela[0] // 4, tamanho_tela[1] - altura_personagem, largura_personagem, altura_personagem
    ))

    pygame.display.update()