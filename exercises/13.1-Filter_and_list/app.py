
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def filtro(nombre):
    return nombre.startswith("R")
resulting_names=list(filter(filtro, all_names))
print(resulting_names)




