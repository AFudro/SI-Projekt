# import the pygame module, so you can use it
import pygame


class Cell:
    def __init__(self):
        data = 'adasda'

class Grid:
    def __init__(self):
        self.gridTab = [ [Cell for x in range(8)] for i in range(8)]
        self.width = 60
        self.height = 60
        self.margin = 10
        self.color = (255, 255, 255)
    def drawGrid(self):
        pygame.init()
        size = (800, 800)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("My Game")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for column in range(0, 8, 1):
                for row in range(0, 8, 1):
                    pygame.draw.rect(screen, self.color, [column*60,row*60,self.width,self.height])
            pygame.display.flip()

def main():
    newGrid = Grid()
    newGrid.drawGrid()

main()
