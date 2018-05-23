import astar

class Vertex:
    def __init__(self,y,x):
        self.x=x
        self.y =y
class Edge:
    def __init__(self,a,b,map):
        self.a=a
        self.b=b
        self.directions = ["W", "N", "E", "S"]
        self.cost=0
        self.path, self.cost =astar.search(self.a.x, self.a.y, self.b.x, self.b.y, self.directions, map)


def find(agentPosition, map, objectmap):
    agentPositionx = agentPosition[0]
    agentPositiony = agentPosition[1]

    vertices=[]
    edges=[]

    vertices.append(Vertex(agentPositionx,agentPositiony))

    for i in range(len(objectmap)):
        for j in range(len(objectmap[0])):
            if (objectmap[i][j] == '1'):
                vertices.append(Vertex(i,j))


    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if(i!=j):
                edges.append(Edge(vertices[i],vertices[j],map))

    array=[]
    for v in vertices:
        array.append([v.x,v.y])

    return array