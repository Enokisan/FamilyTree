import json 
from kanren import Relation, facts, run, conde, var, eq 

with open('relationships.json') as f: 
    d = json.loads(f.read())

father = Relation() 
mother = Relation()

for item in d['father']:
    facts(father, (list(item.keys())[0], list(item.values())[0])) 

for item in d['mother']: 
    facts(mother, (list(item.keys())[0], list(item.values())[0])) 
    
def parent(x, y): 
    return conde((father(x, y),), (mother(x, y),)) 

def grandparent(x, y): 
    temp = var() 
    return conde((parent(x, temp), parent(temp, y))) 

# 要改善
def sibling(x, y): 
    temp = var() 
    return conde((parent(temp, x), parent(temp, y)))  

def uncle(x, y): 
    temp = var()
    return conde((sibling(temp, x), parent(temp, y)))

def cousin(x,y) :
    temp = var()
    return conde((uncle(temp, x), parent(temp, y)))

x = var()