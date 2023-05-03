import random
lista=[]
mayor=0
menor=1000000
tam=random.randint(10, 20)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)
sum=0
cont=0
for h in lista:
    sum+=h
    cont+=1
    if h > mayor:
        mayor=h
    if h < menor:
        menor=h
print(f"La suma es: {sum}")
print(f"El promedio de la suma es: {sum/cont}")
print(f"El mayoe es: {mayor}")
print(f"El menor es: {menor}")

for j in lista:
    resta = j - (sum/cont)
    cuadrado = resta **2
    division = cuadrado / cont
    print(division)

