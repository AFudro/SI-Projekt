import pygame, sys

class Cell(pygame.Rect):
    def __init__(self, x, y, s):
        self.color= (0, 0, 0)
        self.s=s
        super(Cell, self).__init__(x, y, self.s, self.s)
    def draw(self,screen):
        pygame.draw.rect(screen, self.color , self,1)

class Grid:
    def __init__(self,size,cellSize):
        self.size=size
        self.cellSize=cellSize
        self.cells=[[0 for x in range(self.size)] for y in range(self.size)]

        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j]= Cell(i*self.cellSize,j*self.cellSize,self.cellSize)

    def draw(self,screen):
        for i in range(self.size):
            for j in range(self.size):
                self.cells[i][j].draw(screen)

    def getCellSize(self):
        return self.cellSize


class Agent(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("agent.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)




pygame.init()
screen = pygame.display.set_mode((450, 450))

grid= Grid(10,40)


all_sprites = pygame.sprite.Group()
agent = Agent(grid.getCellSize())
all_sprites.add(agent)


while True:
    screen.fill((255, 255, 255))
    grid.draw(screen)

    all_sprites.update()
    all_sprites.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
