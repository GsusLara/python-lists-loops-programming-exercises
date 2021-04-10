arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds(lista):
    total=0
    for i in lista:
        if i%2!=0:
            total+=i
    return(total)

print(sumOdds(arr))
