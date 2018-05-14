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

def generateNeighbors(current,endx,endy):
    neighbors=[]

    if (current.direction[0] == "N"):
        neighbors.append(Node(current.x, current.y-1, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "S"):
        neighbors.append(Node(current.x, current.y+1, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "W"):
        neighbors.append(Node(current.x-1, current.y, current.direction, endx, endy,"move",current.gScore + 1))  # move
    if (current.direction[0] == "E"):
        neighbors.append(Node(current.x+1, current.y, current.direction, endx, endy,"move",current.gScore + 1))  # move

    neighbors.append(
        Node(current.x, current.y, [current.direction[3]] + current.direction[:3], endx, endy,"rotateLeft",current.gScore + 1))  # rotate left
    neighbors.append(
        Node(current.x, current.y, current.direction[1:] + [current.direction[0]], endx, endy,"rotateRight",current.gScore + 1))  # rotate right

    return neighbors

def search():

    startx=5
    starty=2
    endx=3
    endy=4

    start = Node(startx, starty, ["E", "S", "W", "N"], endx, endy, 'start', 0)

    print(start.fScore)
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

        neighbors=generateNeighbors(current,endx,endy)
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

print(search())