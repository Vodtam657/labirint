import pygame

class Wall:

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)


    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 0), self.rect)

pygame.init()

window = pygame.display.set_mode((500, 700))
fps = pygame.time.Clock()

walls = []
walls.append(Wall(100, 20, 30, 50))
walls.append(Wall(100, 20, 30, 130))
walls.append(Wall(130, 120, 30, 30))
walls.append(Wall(160, 120, 30, 80))
walls.append(Wall(30, 170, 160, 30))
walls.append(Wall(30, 170, 30, 150))
walls.append(Wall(30, 300, 320, 30))
walls.append(Wall(320, 320, 30, 110))
walls.append(Wall(30, 400, 320, 30))
walls.append(Wall(30, 400, 30, 110))
walls.append(Wall(100, 20, 30, 50))










while True:
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
    window.fill((0, 0, 0))
    for i in walls:
        i.draw(window)
    pygame.display.flip()

    fps.tick(60)