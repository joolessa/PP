import pygame 
from constantes import *
from assets import *

def tela_inicial(tela):
    clock = pygame.time.Clock()

    #trecho extraido de chat.openai.com
    fonte = pygame.font.Font(None, 60)  # Você também pode fornecer o nome de uma fonte e o tamanho

    # Renderize o texto desejado
    texto = fonte.render("Bem Vindo ao PP game!", True, branco)

    # Posicione o texto no centro da tela
    pos_texto = texto.get_rect(center=(width// 2, height // 2))

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

        tela.blit(texto, pos_texto)

        pygame.display.flip()

    return state