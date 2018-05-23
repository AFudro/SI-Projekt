import pygame
import sys
import astar
import tsp

<<<<<<< HEAD
def loadMap(filepath):
=======
grass = pygame.image.load("sprites/grass.jpg")
tree = pygame.image.load("sprites/tree.jpg")
house = pygame.image.load("sprites/house.jpg")
road = pygame.image.load("sprites/road.jpg")
road2 = pygame.image.load("sprites/road2.jpg")
road3 = pygame.image.load("sprites/road3.jpg")
oil = pygame.image.load("sprites/oil.jpg")
puddle = pygame.image.load("sprites/puddle.jpg")

def loadMap():
>>>>>>> 5be185fbc3ba3f32b4e03cd01f7bdcc1d65687f2
    array = []
    with open(filepath) as f:
        content = f.read().splitlines()
        for line in content:
            array.append(line)
    print(array)
    return array


class Cell(pygame.Rect):
    def __init__(self, x, y, s, wall):
        self.color = (0, 0, 0)
        self.s = s
        self.wall = wall
        self.image = grass
        self.image = pygame.transform.scale(self.image, (40, 40))
        super(Cell, self).__init__(x, y, self.s, self.s)

    def draw(self, screen, color, fill):
        pygame.draw.rect(screen, color, self, fill)
        screen.blit(self.image, self)


class Grid:
    def __init__(self, map, cellSize):
        self.cellSize = cellSize
        self.ysize = len(map)
        self.xsize = len(map[0])
        self.cells = [[0 for x in range(self.xsize)]
                      for y in range(self.ysize)]
        for i in range(self.ysize):
            for j in range(self.xsize):
                self.cells[i][j] = Cell(
                    j * self.cellSize, i * self.cellSize, self.cellSize, int(map[i][j]))

    def draw(self, screen):
        for i in range(self.ysize):
            for j in range(self.xsize):
                if(self.cells[i][j].wall == 0):
                    self.cells[i][j].draw(screen, (255, 0, 0), 0)
                    if( ((i*j)+j+i) % 2 ==0):
                        self.cells[i][j].image = pygame.transform.scale(tree, (40, 40))
                    else:
                        self.cells[i][j].image = pygame.transform.scale(house, (40, 40))
                if(self.cells[i][j].wall == 1):
                    self.cells[i][j].image = pygame.transform.scale(road, (40, 40))
                    self.cells[i][j].draw(screen, (112, 112, 112), 0)
                if(self.cells[i][j].wall == 2):
                    self.cells[i][j].image = pygame.transform.scale(road2, (40, 40))
                    self.cells[i][j].draw(screen, (95, 71, 71), 0)
                if(self.cells[i][j].wall == 3):
                    self.cells[i][j].image = pygame.transform.scale(road3, (40, 40))
                    self.cells[i][j].draw(screen, (95, 71, 71), 0)
                if(self.cells[i][j].wall == 9):
                    self.cells[i][j].image = pygame.transform.scale(oil, (40, 40))
                    self.cells[i][j].draw(screen, (0, 0, 255), 0)
                if(self.cells[i][j].wall == 8):
                    self.cells[i][j].image = pygame.transform.scale(puddle, (40, 40))
                    self.cells[i][j].draw(screen, (0, 255, 0), 0)

    def getCellSize(self):
        return self.cellSize


class TrashCan(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/trashcan.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.size = size


class Agent(pygame.sprite.Sprite):
    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/agent2.png")
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.directions = ["W", "N", "E", "S"]
        self.size = size
        self.path = []

    def rotateRight(self):
        self.image = pygame.transform.rotate(self.image, -90)
        self.directions = self.directions[1:] + [self.directions[0]]

    def rotateLeft(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.directions = [self.directions[3]] + self.directions[:3]

    def move(self):
        if (self.directions[0] == "N"):
            self.rect.center = (
                self.rect.center[0], self.rect.center[1] - self.size)
        if (self.directions[0] == "S"):
            self.rect.center = (
                self.rect.center[0], self.rect.center[1] + self.size)
        if (self.directions[0] == "W"):
            self.rect.center = (
                self.rect.center[0] - self.size, self.rect.center[1])
        if (self.directions[0] == "E"):
            self.rect.center = (
                self.rect.center[0] + self.size, self.rect.center[1])

    def goTo(self, endy, endx):
        if(int(map[int(self.rect.y / self.size)][int(self.rect.x / self.size)]) > 0):
            agentPositionx = self.rect.x / self.size
            agentPositiony = self.rect.y / self.size
            print(agentPositionx, agentPositiony)
            self.path = astar.search(
                agentPositionx, agentPositiony, endx, endy, self.directions, map)
            print(self.path)
        else:
            self.path = []

    def update(self):
        if self.path:
            action = self.path.pop(0)
            if (action == 'rotateRight'):
                self.rotateRight()
            if (action == 'rotateLeft'):
                self.rotateLeft()
            if (action == 'move'):
                self.move()


pygame.init()
screen = pygame.display.set_mode((1200, 900))


cellSize=40

map = loadMap('map.txt')
objectmap=loadMap('objectmap.txt')
grid = Grid(map, cellSize)

all_sprites = pygame.sprite.Group()
agent = Agent(grid.getCellSize())
all_sprites.add(agent)


for i in range(len(objectmap)):
    for j in range(len(objectmap[0])):
        if (objectmap[i][j]=='1'):
            all_sprites.add(TrashCan(cellSize,(j*cellSize)+20,i*cellSize+20))

clock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))
    grid.draw(screen)

    all_sprites.update()
    all_sprites.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i in range(grid.ysize):
                for j in range(grid.xsize):
                    if(grid.cells[i][j].collidepoint(pos)):
                        print(i, j)
                        agent.goTo(i, j)
                        tsp.find(agent,map,objectmap)
                        break
    pygame.display.update()
    clock.tick(15)
