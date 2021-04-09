#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:
for i in range(10):
    numero=random.randint(0,99)
    my_list.append(numero)

print(my_list)