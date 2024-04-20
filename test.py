import pygame

class Wall:
     def __init__(self, x, y, w, h):
         self.rect = pygame.Rect(x, y, w, h):

         def draw(self, window):
             pygame.draw.rect(window, (255, 255, 0))

pygame.init()

window = pygame.display.set_mode((500,700))
fps = pygame.time.Clock()

walls = []
walls.append(
    Wall(0, 100, 30, 200)


game = True
while True:
    for event in pygame.event.get():
        if ev.type  == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        window.fill((0, 50, 0))
        for i in walls:
            i.draw(window, (255, 0, 255))

    pygame.display.flip()

    for wall in walls:
        if wall.rect.collidepoint(player.hitbox):
            game = False


    fps.tick(60)