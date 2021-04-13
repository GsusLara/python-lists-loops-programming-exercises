parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot(matriz):
    salida={
        "totalSlots":0,
        "availableSlots":0,
        "occupiedSlots":0
    }
    for i in parking_state:
        for j in i:
            if j==1:
                salida["totalSlots"]+=1
                salida["availableSlots"]+=1
            elif j==2:
                salida["totalSlots"]+=1
                salida["occupiedSlots"]+=1
            else:
                pasillo=1
    return(salida)
updatedState=get_parking_lot(parking_state)
print(updatedState)