import pygame, sys
from pygame.locals import *


class Grid:
    def __init__(self, x,y ):
        pass



class Cell(pygame.Rect):
    def __init__(self, x, y):
        self.color= (0, 0, 255)
        self.s=20
        super(Cell, self).__init__(x, y, self.s, self.s)
    def draw(self,screen):
        pygame.draw.rect(screen, color , self)


class Agent:
    pass


pygame.init()
screen = pygame.display.set_mode((400, 300))



cell= Cell(11,26)
cell.draw(screen)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()