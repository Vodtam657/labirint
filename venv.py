import pygame

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()



background = pygame.transform.scale(pygame.image.load("images (2).jpg"), (700, 500))




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.blit(background, (0, 0))
    roma.draw(window)
    roma.move()
    salabai.draw(window)
    salabai.move()

    pygame.display.flip()
    fps.tick(60)