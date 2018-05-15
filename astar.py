from math import *
import operator

index=0

class Node:
    def __init__(self,x,y,direction,endx,endy,action,gScore):
        global index
        self.id=index
        index=index+1

        self.gScore=gScore
        self.hScore=sqrt(((x-endx)**2)+((y-endy)**2))
        self.fScore=self.gScore+self.hScore
        self.visitedBy=0
        self.x=x
        self.y=y
        self.direction=direction
        self.action=action


    def update(self):
        self.fScore=self.gScore+self.hScore

def generateNeighbors(current,endx,endy,grid):
    neighbors=[]
    #print(current.x, current.y-1)
    if (current.direction[0] == "N"):
        if((current.y-1)>=0):
            if(grid[int(current.x)][int(current.y-1)].wall==0):
                neighbors.append(Node(current.x, current.y-1, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "S"):
        if((current.y+1)<len(grid)):
            if(grid[int(current.x)][int(current.y+1)].wall==0):
                neighbors.append(Node(current.x, current.y+1, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "W"):
        if((current.x-1)>=0):
            if(grid[int(current.x-1)][int(current.y)].wall==0):
                neighbors.append(Node(current.x-1, current.y, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "E"):
        if((current.x+1)<len(grid)):
            if(grid[int(current.x+1)][int(current.y)].wall==0):
                neighbors.append(Node(current.x+1, current.y, current.direction, endx, endy,"move",current.gScore + 1))  # move

    neighbors.append(
        Node(current.x, current.y, [current.direction[3]] + current.direction[:3], endx, endy,"rotateLeft",current.gScore + 1))  # rotate left
    neighbors.append(
        Node(current.x, current.y, current.direction[1:] + [current.direction[0]], endx, endy,"rotateRight",current.gScore + 1))  # rotate right

    return neighbors

def search(startx,starty,endx,endy,startdirection,grid):
    start = Node(startx, starty, startdirection, endx, endy, 'start', 0)

    closedSet =[]
    openSet = [start]
    start.gScore=0

    while openSet:
        openSet.sort(key=operator.attrgetter('fScore'))
        current = openSet[0]

        if current.hScore==0:
            return reconstruct_path(closedSet, current)

        openSet.remove(current)
        closedSet.append(current)

        neighbors=generateNeighbors(current,endx,endy,grid)
        for neighbor in neighbors:
            if neighbor in closedSet:
                continue		#Ignore the neighbor which is already evaluated.

            if neighbor not in openSet:
                openSet.append(neighbor)

            tentative_gScore = current.gScore + 1
            neighbor.visitedBy=current.id
            neighbor.gScore=tentative_gScore
            neighbor.update()

    return 0

def reconstruct_path(closedSet, current):
    total_path = [current.action]

    while current.action!="start":
        for x in closedSet:
            if x.id == current.visitedBy:
                current=x
                total_path.append(current.action)
    total_path.reverse()
    return total_path

# print(search())
