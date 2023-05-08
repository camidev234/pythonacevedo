import random

# nota =round(nota,2)
lon = random.randrange(20, 30)

lista = [round(random.random()*5,1)   for i in range(lon)]
print(lista)
for n in range(lon):
    for j in range(n+1, lon):
        if lista[n] > lista[j]:
            aux=lista[n]
            lista[n] = lista[j]
            lista[j] = aux

print(lista)
    
# lista2 = [x for x in lista if x >= 3]
# print("lista de buenos", lista2)
# lista3= [j for j in lista if j < 3]
# print("lista de reprobados", lista3)
# listag1 = [c for c in lista if c <1]
# print("grupo de 0 a 1",listag1)
# listag2= [f for f in lista if f >=1 and f <2]
# print("grupo de 1 a 2", listag2)
# listag3= [o for o in lista if o >=2 and o <3]
# print("grupo de 2 a 3",listag3)
# listag4= [p for p in lista if p if p >=3 and p <4]
# print("grupo de 3 a 4",listag4)
# listag5=[a for a in lista if a >=4 and a<=5]
# print("grupo de 4 a 5",listag5)