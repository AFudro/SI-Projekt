from math import *
import operator
from queue import *

index = 0


class Node:
    def __init__(self, x, y, direction, endx, endy, action, gScore):
        self.gScore = gScore
        self.hScore = sqrt(((endx - x)**2) + ((endy - y)**2))
        self.fScore = self.gScore + self.hScore
        self.x = x
        self.y = y
        self.direction = direction
        self.action = action

    def __lt__(self, other):
        return self.fScore < other.fScore

    def update(self):
        self.fScore = self.gScore + self.hScore


def generateNeighbors(current, endx, endy, map):
    neighbors = []
    # print(current.x, current.y-1)
    if (current.direction[0] == "N"):
         if((current.y - 1) >= 0):
             if(map[int(current.y - 1)][int(current.x)] != '0'):
                neighbors.append(Node(current.x, current.y - 1, current.direction, endx, endy, "move",
                                 current.gScore + current.gScore + int(map[int(current.y - 1)][int(current.x)])))  # move
    if (current.direction[0] == "S"):
         if((current.y + 1) < len(map)):
             if(map[int(current.y + 1)][int(current.x)] != '0'):
                neighbors.append(Node(current.x, current.y + 1, current.direction, endx, endy, "move",
                                 current.gScore + current.gScore + int(map[int(current.y + 1)][int(current.x)])))  # move
    if (current.direction[0] == "W"):
         if((current.x - 1) >= 0):
             if(map[int(current.y)][int(current.x - 1)] != '0'):
                neighbors.append(Node(current.x - 1, current.y, current.direction, endx, endy, "move",
                                 current.gScore + current.gScore + int(map[int(current.y)][int(current.x - 1)])))  # move
    if (current.direction[0] == "E"):
         if((current.x + 1) < len(map[0])):
            if(map[int(current.y)][int(current.x + 1)] != '0'):
                neighbors.append(Node(current.x + 1, current.y, current.direction, endx, endy, "move",
                                 current.gScore + current.gScore + int(map[int(current.y)][int(current.x + 1)])))  # move

    neighbors.append(
        Node(current.x, current.y, [current.direction[3]] + current.direction[:3], endx, endy, "rotateLeft", current.gScore + 1))  # rotate left
    neighbors.append(
        Node(current.x, current.y, current.direction[1:] + [current.direction[0]], endx, endy, "rotateRight", current.gScore + 1))  # rotate right

    return neighbors


def search(startx, starty, endx, endy, startdirection, map):
    start = Node(startx, starty, startdirection, endx, endy, 'start', 0)

    closedSet = set()
    openSet = PriorityQueue()
    openSet.put((start.fScore, start.x, start.y, start.direction[0], start))
    start.gScore = 0
    cameFrom = {}

    while not openSet.empty():
        current = openSet.get()[4]
        if current.hScore == 0:
            return reconstruct_path(cameFrom, current)
        closedSet.add(str(current.x) + ',' + str(current.y) +
                      ',' + current.direction[0] + ',')

        for neighbor in generateNeighbors(current, endx, endy, map):
            if str(neighbor.x) + ',' + str(neighbor.y) + ',' + neighbor.direction[0] + ',' in closedSet:
                continue
            if (neighbor.fScore, neighbor.x, neighbor.y, neighbor.direction[0], neighbor) not in openSet.queue:
                openSet.put((neighbor.fScore, neighbor.x,
                            neighbor.y, neighbor.direction[0], neighbor))
            if neighbor.action == "move":
                tentative_gScore = current.gScore + int(map[int(neighbor.y)][int(neighbor.x)])
            else:
                tentative_gScore = current.gScore + int(map[int(neighbor.y)][int(neighbor.x)])
            cameFrom[neighbor]=current
            neighbor.gScore=tentative_gScore
            neighbor.update()

    return 0

def reconstruct_path(cameFrom, current):
    total_path=[current.action]
    while current.action != "start":
        current=cameFrom[current]
        total_path.append(current.action)
    total_path.reverse()
    return total_path

# print(search())
