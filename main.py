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
        self.directions=["W","N","E","S"]
        self.size=size
    def rotateRight(self):
        self.image = pygame.transform.rotate(self.image, -90)
        self.directions= self.directions[1:]+ [self.directions[0]]
    def rotateLeft(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.directions= [self.directions[3]]+self.directions[:3]

    def move(self):
        if (self.directions[0]=="N"):
            self.rect.center = (self.rect.center[0] , self.rect.center[1]- self.size)
        if (self.directions[0]=="S"):
            self.rect.center = (self.rect.center[0] , self.rect.center[1] + self.size)
        if (self.directions[0]=="W"):
            self.rect.center = (self.rect.center[0] - self.size, self.rect.center[1] )
        if (self.directions[0]=="E"):
            self.rect.center = (self.rect.center[0] + self.size, self.rect.center[1] )




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

    print(agent.directions)
    print(agent.rect.center)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                agent.rotateLeft()
            if event.key == pygame.K_RIGHT:
                agent.rotateRight()
            if event.key == pygame.K_UP:
                agent.move()


    pygame.display.update()
