people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    salida=[]
    for i in people:
        if i!=person_name:
            salida.append(i)
    return salida        
    #Your code go here:
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))