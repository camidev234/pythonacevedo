import math
import random
lista=[]
mayor=0
menor=1000000
suma=0
sum=0
cont=0
tam=random.randint(10, 20)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)
for h in lista:
    sum+=h
    cont+=1
    if h > mayor:
        mayor=h
    if h < menor:
        menor=h
print(f"La suma es: {sum}")
print(f"El promedio es: {sum/cont}")
print(f"El mayoe es: {mayor}")
print(f"El menor es: {menor}")

for j in lista:
    resta = j - (sum/cont)
    cuadrado = resta **2
    suma+=cuadrado
    division = suma // cont
raiz = math.sqrt(division)
print(f"La desviacion estandar es: {raiz}")

maxRep=0

for numAct in lista:
    cont=0
    for s in lista:
        if numAct == s:
            cont+=1
    if cont > maxRep:
        maxRep=cont
        moda=numAct
   
print(f"La moda es {moda}")