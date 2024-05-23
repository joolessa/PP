import pygame 
from constantes import *
from assets import *

pygame.init()

def tela_inicial(tela):
    clock = pygame.time.Clock()  

    #trecho extraido de chat.openai.com
    fonte = pygame.font.Font(None, 40) # Você também pode fornecer o nome de uma fonte e o tamanho

    # Renderize o texto desejado
    texto1 = fonte.render("Bem Vindo ao PP game!", True, branco)
    texto2 = fonte.render("Clique para iniciar e solte sua voz!", True, branco)
    texto3 = fonte.render("Bob, o minion, moverá para cima ou para baixo de acordo com a sua voz!", True, branco)
    texto4 = fonte.render("Controle seu vozerão para não deixar ele tocar nos espinhos do teto,", True, branco)
    texto5 = fonte.render("do piso e os que estão vindo em sua direção da direita!", True, branco)

    # Posicione o texto no centro da tela
    pos_texto1 = texto1.get_rect(center=((width// 2), (height // 2)-200))
    pos_texto2 = texto2.get_rect(center=((width// 2)-10, (height // 2)+350))
    pos_texto3 = texto4.get_rect(center=((width// 2)-20, (height // 2)-100))
    pos_texto4 = texto4.get_rect(center=((width// 2)-10, (height // 2)+150))
    pos_texto5 = texto4.get_rect(center=((width// 2)+80, (height // 2)+180))

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
        tela.blit(texto3, pos_texto3)
        tela.blit(texto4, pos_texto4)
        tela.blit(texto5, pos_texto5)

        pygame.display.flip()

    return state

tela = pygame.display.set_mode((width, height))
pygame.display.set_caption('PP GAME')
tela_inicial(tela)