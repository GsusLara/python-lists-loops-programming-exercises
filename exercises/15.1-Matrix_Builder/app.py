#Import random

#Create the function below:
def matrixBuilder(n):
    salida=[]
    for i in range(n):
        salida.append([])
        for j in range(n):
            salida[i].append(1)
    return(salida)

print(matrixBuilder(5))