import random
import math
lista1 = [random.randrange(30) for i in range(10)]
print(lista1)
lista2=[math.sqrt(x) if x % 2==0 else x **2 for x in lista1]
print(lista2)