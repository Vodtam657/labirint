import pygame

from est import Bulba
from salabai import Salabai

window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()



background = pygame.transform.scale(pygame.image.load("black.background.png"), (700, 500))

est = Bulba(100, 100, 50, 50, "images.png", 2)
salabai = Salabai(100, 100, 50, 50, "images.png", 2, 200, 200)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    salabai.rux()

    window.blit(background, (0, 0))

    salabai.draw(window)
    est.draw(window)


    pygame.display.flip()
    fps.tick(60)