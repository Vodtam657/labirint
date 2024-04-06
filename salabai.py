import pygame, sys


class Salabai:
    def __init__ (self, x, y, w, h, img,speed, entx, enty):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w,h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.endx = entx
        self.endy = enty
        self.x = x
        self.y = y



    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))


    def rux (self):
        if self.endx >= self.hitbox.x:
            self.speed *= -1
        if self.x <= self.hitbox.x:
            self.speed *= -1
        self.hitbox.x+= self.speed

