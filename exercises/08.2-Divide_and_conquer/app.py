list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(numeros):
    even=[]
    odd=[]
    salida=[]
    for i in numeros:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    salida.append(odd)
    salida.append(even)
    return(salida)   

print(merge_two_list(list_of_numbers))

