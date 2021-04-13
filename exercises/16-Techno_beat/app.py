def lyrics_generator(beat):
    salida=""
    bass=0
    for i in beat:
        if i ==0:
            salida+="Boom "
        else:
            if bass==2:
                salida+="Drop the base !!!Break the base!!! "
                bass=0
            else:
                bass=bass+1
                salida+="Drop the base "
    return(salida)

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))