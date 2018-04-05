import pygame, sys
from pygame.locals import *

class Cell(pygame.Rect):
    def __init__(self, x, y, s):
        self.color= (0, 0, 255)
        self.s=s
        super(Cell, self).__init__(x, y, self.s, self.s)
    def draw(self,screen):
        pygame.draw.rect(screen, self.color , self,1)

class Grid:
    def __init__(self):
        self.size=50
        self.cellSize=20
        self.cells=[[0 for x in range(self.size)] for y in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j]= Cell(i*self.cellSize,j*self.cellSize,self.cellSize)

    def draw(self,screen):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].draw(screen)






class Agent:
    pass


pygame.init()
screen = pygame.display.set_mode((400, 300))

# cell= Cell(11,26)
# cell.draw(screen)
grid= Grid()
grid.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()