theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def selector(x):
    if x ==1:
        return 'wiki'
    else:
        return 'woko'

salida=list(map(selector,theBools))
print(salida)
