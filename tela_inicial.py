import pygame 
from constantes import *
from assets import *

pygame.init()

def tela_inicial(tela):
    clock = pygame.time.Clock()  

    #trecho extraido de chat.openai.com
    fonte = pygame.font.Font(None, 60) # Você também pode fornecer o nome de uma fonte e o tamanho

    # Renderize o texto desejado
    texto1 = fonte.render("Bem Vindo ao PP game!", True, branco)
    texto2 = fonte.render("Clique para iniciar e solte sua voz!", True, branco)
    texto3 = fonte.render("Feito por Joana, Maria e Valentina", True, branco)

    # Posicione o texto no centro da tela
    pos_texto1 = texto1.get_rect(center=((width// 2), (height // 2)-200))
    pos_texto2 = texto2.get_rect(center=((width// 2)-10, (height // 2)-100))
    pos_texto3 = texto3.get_rect(center=((width// 2)-10, (height // 2)))

    #trecho extraido de https://dessoft.insper-comp.com.br/conteudo/projeto
    running = True
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = FIM
                running = False

            if event.type == pygame.KEYUP:
                state = JOGO
                running = False

        tela.fill(preto)

        tela.blit(texto1, pos_texto1)
        tela.blit(texto2, pos_texto2)

        pygame.display.flip()

    return state

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('PP GAME')
tela_inicial(tela)