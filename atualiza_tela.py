def atualizar_tela(tela, fonte, retangulo_personagem, volume):
    tela.fill((255, 255, 255))
    pygame.draw.rect(tela, (0, 0, 255), retangulo_personagem)
    texto_volume = fonte.render(f"Volume: {volume:.2f}", True, (0, 0, 0))
    retangulo_texto = texto_volume.get_rect()
    retangulo_texto.topright = (TAMANHO_DA_TELA[0] - 10, 10)
    tela.blit(texto_volume, retangulo_texto)
    pygame.display.update()
