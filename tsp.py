import astar
import random
import math



def crossover(a,b):
    n = len(a)
    point= random.randint(1, n - 2)
    c1 = a[:point]
    for i in b:
        if i not in c1:
            c1.append(i)
    c2 = b[:point]
    for i in a:
        if i not in c2:
            c2.append(i)
    return (c1,c2)

def mutation(individual):
    probability=0.02
    if (random.random()<= probability):
        i= random.randint(1, len(individual)-1)
        j= random.randint(1, len(individual)-1)
        individual[i], individual[j]= individual[j], individual[i]

def fitness(individual,edges):
    distance=0
    # print(individual)
    for i in range(len(individual)-1):
        for e in edges:
            if (e.a.id==individual[i] and e.b.id==individual[i+1]):
                distance += e.cost
                # print(e.a.id, e.b.id, e.cost)
    return distance



def initPopulation(length):
    population=[]
    populationSize=10*length
    if (populationSize > math.factorial(length-1)):
        populationSize= math.factorial(length-1)
    while len(population)<populationSize:
        individual=list(range(1,length))
        random.shuffle(individual)
        individual=[0]+individual
        if (individual not in population):
            population.append(individual)
    return population


class Vertex:
    def __init__(self,id,y,x):
        self.id=id
        self.x=x
        self.y =y
class Edge:
    def __init__(self,a,b,map):
        self.a=a
        self.b=b
        self.directions = ["N", "E", "S","W"]
        self.cost=0
        self.path, self.cost =astar.search(self.a.x, self.a.y, self.b.x, self.b.y, self.directions, map)


def find(agentPosition, map, objectmap):
    agentPositionx = agentPosition[0]
    agentPositiony = agentPosition[1]

    vertices=[]
    edges=[]
    vertices.append(Vertex(0,agentPositionx,agentPositiony))
    index=1
    for i in range(len(objectmap)):
        for j in range(len(objectmap[0])):
            if (objectmap[i][j] == '1'):
                vertices.append(Vertex(index,i,j))
                index +=1
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if(i!=j):
                edges.append(Edge(vertices[i],vertices[j],map))

    population=initPopulation(len(vertices))
    populationSize= len(population)
    population.sort(key= lambda x : fitness(x, edges))
    iterations=100
    j=0

    children=[]
    while j<iterations:
        j+=1
        for x in range(0, len(population), 2):
            parent1=population[x]
            parent2=population[x+1]
            children1, children2 = crossover(parent1,parent2)
            mutation(children1)
            mutation(children2)
            children.append(children1)
            children.append(children2)
        for c in children:
            if c not in population:
                population.append(c)
        population.sort(key= lambda x : fitness(x, edges))
        del population[populationSize:]

    for p in population:
        print(p, fitness(p,edges))

    best= population[0]
    path=[]
    for v in best:
        path.append([vertices[v].x, vertices[v].y])
    print(path)


    return path