from math import *
import operator
class Node:
    def __init__(self,x,y,direction,endx,endy,action):
        self.gScore=0
        self.hScore=sqrt(((x-endx)**2)+((y-endy)**2))
        self.fScore=self.gScore+self.hScore
        self.visitedBy=0
        self.x=x
        self.y=y
        self.direction=direction
        self.action=action


    def update(self):
        self.fScore=self.fScore=self.gScore+self.hScore



def generateNeighbors(current,endx,endy):
    neighbors=[]

    if (current.direction[0] == "N"):
        neighbors.append(Node(current.x, current.y+1, current.direction, endx, endy,"move"))  # move
    if (current.direction[0] == "S"):
        neighbors.append(Node(current.x, current.y-1, current.direction, endx, endy,"move"))  # move
    if (current.direction[0] == "W"):
        neighbors.append(Node(current.x-1, current.y, current.direction, endx, endy,"move"))  # move
    if (current.direction[0] == "E"):
        neighbors.append(Node(current.x+1, current.y, current.direction, endx, endy,"move"))  # move

    neighbors.append(
        Node(current.x, current.y, [current.direction[3]] + current.direction[:3], endx, endy,"rotateLeft"))  # rotate left
    neighbors.append(
        Node(current.x, current.y, current.direction[1:] + [current.direction[0]], endx, endy,"rotateRight"))  # rotate right

    return neighbors

def search():

    startx=0
    starty=0
    endx=1
    endy=1

    start = Node(startx,starty,["W", "N", "E", "S"],endx,endy,'start')
    end = Node(endx,endy,'',endx,endy,'end')

    print(start.fScore)
    print(end.fScore)
    # The set of nodes already evaluated
    closedSet =[]

    # The set of currently discovered nodes that are not evaluated yet.
    # Initially, only the start node is known.
    openSet = [start]

    # For each node, which node it can most efficiently be reached from.
    # If a node can be reached from many nodes, cameFrom will eventually contain the
    # most efficient previous step.
    cameFrom = []

    # For each node, the cost of getting from the start node to that node.
    #gScore := map with default value of Infinity

    # The cost of going from start to start is zero.
    #gScore[start] := 0
    start.gScore=0


    # For each node, the total cost of getting from the start node to the goal
    # by passing by that node. That value is partly known, partly heuristic.
    #fScore := map with default value of Infinity

    # For the first node, that value is completely heuristic.
    #fScore[start] := heuristic_cost_estimate(start, goal)

    while openSet:
        openSet.sort(key=operator.attrgetter('fScore'))
        current = openSet[0]

        if current.hScore==0:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closedSet.append(current)

        neighbors=generateNeighbors(current,endx,endy)
        for neighbor in neighbors:
            if neighbor in closedSet:
                continue		#Ignore the neighbor which is already evaluated.

            if neighbor not in openSet:	#Discover a new node
                openSet.append(neighbor)

            # The distance from start to a neighbor
            #the "dist_between" function may vary as per the solution requirements.




            tentative_gScore = current.gScore + 1

            if tentative_gScore >= neighbor.gScore:
                continue		# This is not a better path.

            # This path is the best until now. Record it!
            cameFrom.append(current)
            neighbor.visitedBy=current
            neighbor.gScore=tentative_gScore
            neighbor.update()

    return 0

def reconstruct_path(closedSet, current):
    for x in closedSet:
        print(x.action)
    total_path = [current.action]
    while current in closedSet:
        current = closedSet[current]
        total_path.append(current.action)
    return total_path

print(search())