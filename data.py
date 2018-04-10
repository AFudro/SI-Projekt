from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y')
pyDatalog.create_terms('trash') # type of item
pyDatalog.create_terms('plasticContainer,paperContainer,organicContainer,glassContainer,mixedContainer') # types of containers
pyDatalog.create_terms('plastic,glass,paper,cardboard,organic') # material
pyDatalog.create_terms('color,elastic,fragile,white,containsInk') # properties


trash['unknownObject2']=1
color['unknownObject2']=1
fragile['unknownObject2']=0.8

trash['unknownObject1']=1
color['unknownObject1']=1
elastic['unknownObject1']=1

trash['unknownObject3']=1
white['unknownObject3']=0.8
containsInk['unknownObject3']=0.6

plastic(X) <= (trash[X]==1) & (color[X]==1) & (elastic[X]>0.8)
glass(X) <= (trash[X]==1) & (color[X]==1) & (fragile[X]>0.5)
paper(X) <= (trash[X]==1) & (white[X]>0.5) & (containsInk[X]>0.3)
glassContainer(X) <= glass(X)
plasticContainer(X) <= plastic(X)
paperContainer(X) <= paper(X)
print(paperContainer(X))

